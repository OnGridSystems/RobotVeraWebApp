# Generated by Django 2.0.3 on 2018-06-28 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0006_auto_20180628_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledmeeting',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scheduledmeeting',
            name='date',
            field=models.DateField(),
        ),
    ]