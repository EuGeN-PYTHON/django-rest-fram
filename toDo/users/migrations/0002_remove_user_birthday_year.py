# Generated by Django 3.2.9 on 2021-11-16 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday_year',
        ),
    ]