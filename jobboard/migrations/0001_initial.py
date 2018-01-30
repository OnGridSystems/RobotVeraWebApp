# Generated by Django 2.0 on 2018-01-09 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_address', models.CharField(blank=True, max_length=64, null=True)),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('snails', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CurriculumVitae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('salary_from', models.PositiveIntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobboard.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_address', models.CharField(blank=True, max_length=64, null=True)),
                ('organization', models.CharField(max_length=255)),
                ('inn', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('parent_specialisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobboard.Specialisation')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('salary_from', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('salary_up_to', models.PositiveIntegerField(blank=True, null=True)),
                ('salary_by_agreement', models.BooleanField(default=False)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobboard.Employer')),
                ('keywords', models.ManyToManyField(to='jobboard.Keyword')),
                ('specializations', models.ManyToManyField(to='jobboard.Specialisation')),
            ],
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='keywords',
            field=models.ManyToManyField(to='jobboard.Keyword'),
        ),
        migrations.AddField(
            model_name='curriculumvitae',
            name='specializations',
            field=models.ManyToManyField(to='jobboard.Specialisation'),
        ),
    ]