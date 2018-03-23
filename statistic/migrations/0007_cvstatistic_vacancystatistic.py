# Generated by Django 2.0.2 on 2018-03-22 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('statistic', '0006_auto_20180322_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='CvStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('ip', models.GenericIPAddressField()),
                ('session_id', models.CharField(max_length=32)),
                ('count', models.PositiveIntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('elem_object_id', models.PositiveIntegerField()),
                ('elem_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cv_stats', to='contenttypes.ContentType')),
                ('role_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'CV statistic',
            },
        ),
        migrations.CreateModel(
            name='VacancyStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_object_id', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('ip', models.GenericIPAddressField()),
                ('session_id', models.CharField(max_length=32)),
                ('count', models.PositiveIntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('elem_object_id', models.PositiveIntegerField()),
                ('elem_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vac_stats', to='contenttypes.ContentType')),
                ('role_content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Vacancy statistic',
            },
        ),
    ]
