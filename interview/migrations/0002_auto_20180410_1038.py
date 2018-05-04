# Generated by Django 2.0.3 on 2018-04-10 10:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_curriculumvitae_enabled'),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actioninterview',
            name='interviewer',
            field=models.CharField(choices=[('Me', 'me'), ('Vera', 'vera')], default='me', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interviewpassed',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='interviewpassed',
            name='cv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interviews', to='cv.CurriculumVitae'),
        ),
        migrations.AddField(
            model_name='interviewpassed',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interviewpassed',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
