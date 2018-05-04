# Generated by Django 2.0.3 on 2018-04-11 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_auto_20180411_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interview',
            name='vacancy',
        ),
        migrations.RemoveField(
            model_name='interviewpassed',
            name='cv',
        ),
        migrations.AlterField(
            model_name='interviewpassed',
            name='interview',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='passed', to='interview.Interview'),
        ),
    ]
