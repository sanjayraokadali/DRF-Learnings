# Generated by Django 3.1.4 on 2021-01-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=60)),
                ('company_email', models.EmailField(max_length=60)),
                ('job_title', models.CharField(max_length=60)),
                ('job_description', models.TextField()),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
