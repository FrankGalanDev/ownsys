# Generated by Django 3.1.1 on 2021-03-12 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categdoc',
            old_name='categdoc',
            new_name='categdoc_name',
        ),
        migrations.RenameField(
            model_name='categtask',
            old_name='category_task',
            new_name='category_task_name',
        ),
    ]