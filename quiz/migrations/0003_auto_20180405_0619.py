# Generated by Django 2.0.3 on 2018-04-05 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20180403_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionexam',
            name='action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exam', to='pipeline.Action'),
        ),
    ]