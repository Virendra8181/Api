# Generated by Django 4.1.3 on 2022-11-01 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
    ]
