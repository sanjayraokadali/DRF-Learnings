# Generated by Django 3.1.4 on 2021-01-16 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name']},
        ),
    ]
