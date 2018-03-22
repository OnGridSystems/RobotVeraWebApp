from vera.celery import app
from celery.app.task import Task
from quiz.models import ExamPassing, Answer, AnswerForVerification
import numpy as np
import requests
from sklearn.metrics.pairwise import euclidean_distances
from nltk.corpus import stopwords
from nltk import word_tokenize
from django.conf import settings


class ProcessExam(Task):
    name = 'ProcessExam'
    soft_time_limit = 10 * 60
    default_retry_delay = 10

    def __init__(self):
        self.instance = None
        self.total_count = 0
        self.w2v_handler = VeraW2V()

    def run(self, instance_id, *args, **kwargs):
        try:
            self.instance = ExamPassing.objects.get(pk=instance_id)
        except ExamPassing.DoesNotExist:
            # TODO what is DoesNotExist?
            pass
        else:
            self.handle_exam()
            self.instance.points = self.total_count
            self.instance.processed = True
            self.instance.save()
        return True

    def handle_exam(self):
        for item in self.instance.exam.questions.all():
            candidate_answer = self.instance.answers.get('question_' + str(item.id), None)
            if candidate_answer is None:
                continue
            if item.kind.w2v:
                self.process_w2w_question(item, candidate_answer)
            else:
                if isinstance(candidate_answer, list):
                    self.handle_answer(sum(
                        [answer['weight'] for answer in
                         Answer.objects.values('weight').filter(pk__in=candidate_answer)]),
                        item.weight)
                elif isinstance(candidate_answer, str) or isinstance(candidate_answer, int):
                    self.handle_answer(Answer.objects.get(pk=int(candidate_answer)).weight, item.weight)

    def process_w2w_question(self, question, candidate_answer):
        w2v_total = 0
        min_sim = 1
        for answer in question.answers.all():
            self.w2v_handler.set_answers(right_answer=answer.text, candidate_answer=candidate_answer)
            sim = self.w2v_handler.run()
            if sim < min_sim and isinstance(sim, float):
                w2v_total = (1 - sim) * answer.weight
        self.total_count += w2v_total * question.weight

    def handle_answer(self, weight, qe_weight):
        self.total_count += weight * qe_weight

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('Возникла ошибка: {}'.format(exc))
        self.retry()
        pass


class VeraW2V(object):

    def __init__(self):
        self.stop = set(stopwords.words('english'))
        self.stop.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
        self.api_url = settings.W2V_API_URL
        self.candidate_answer = None
        self.right_answer = None
        self.similarity = 0

    def run(self):
        if not (self.candidate_answer or self.right_answer):
            return False
        self.get_similarity_euql()
        return self.similarity

    def set_answers(self, right_answer, candidate_answer):
        self.right_answer = right_answer
        self.candidate_answer = candidate_answer

    def get_similarity_euql(self):
        right_sentence = [i for i in word_tokenize(self.right_answer.lower()) if i not in self.stop]
        candidate_sentence = [i for i in word_tokenize(self.candidate_answer.lower()) if i not in self.stop]
        if not bool(len(right_sentence)) or not bool(len(candidate_sentence)):
            return False
        for i in right_sentence:
            first_vector = requests.post(self.api_url, data={"word": i}).text
            try:
                first_vector = np.asarray(eval(first_vector), dtype=np.float32)
            except SyntaxError:
                pass
            else:
                sim_i = 0
                for j in candidate_sentence:
                    second_vector = requests.post(self.api_url, data={"word": j}).text
                    try:
                        second_vector = np.asarray(eval(second_vector), dtype=np.float32)
                    except SyntaxError:
                        pass
                    else:
                        sim_i += euclidean_distances(first_vector.reshape(-1, 1), second_vector.reshape(-1, 1))[0][0]
                self.similarity += sim_i / len(candidate_sentence)
        self.similarity = self.similarity / len(right_sentence)


class VerifyAnswer(Task):
    name = 'VerifyAnswer'
    soft_time_limit = 10 * 60

    def __init__(self):
        self.instance = None
        self.w2v_handler = VeraW2V()

    def run(self, instance_id, *args, **kwargs):
        self.instance = AnswerForVerification.objects.get(pk=instance_id)
        self.verify()
        return True

    def verify(self):
        answers = self.instance.question.answers.all()
        min_sim = 1
        related_answer = None
        for answer in answers:
            self.w2v_handler.set_answers(answer.text, self.instance.answer)
            sim = self.w2v_handler.run()
            if sim < min_sim:
                min_sim = sim
                related_answer = answer
        self.instance.related_answer = related_answer
        self.instance.points = ((1 - min_sim) * related_answer.weight) * self.instance.question.weight
        self.instance.processed = True
        self.instance.save()


app.register_task(ProcessExam())
app.register_task(VerifyAnswer())