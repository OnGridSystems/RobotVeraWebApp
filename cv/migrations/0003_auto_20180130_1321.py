# Generated by Django 2.0 on 2018-01-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20180130_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='level',
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.EducationLevel'),
        ),
    ]
