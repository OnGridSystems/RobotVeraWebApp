# Generated by Django 2.0 on 2018-01-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0004_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='contract_address',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]