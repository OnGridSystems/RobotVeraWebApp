# Generated by Django 2.0.2 on 2018-03-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0003_auto_20180321_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvstatistic',
            name='session_id',
            field=models.CharField(default='zujesb1vhs3warp9jpr6pk9vc9thhgag', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancystatistic',
            name='session_id',
            field=models.CharField(default='zujesb1vhs3warp9jpr6pk9vc9thhgag', max_length=32),
            preserve_default=False,
        ),
    ]