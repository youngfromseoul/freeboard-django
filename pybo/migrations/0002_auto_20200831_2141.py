# Generated by Django 3.0.7 on 2020-08-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qustion',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='qustion',
            new_name='question',
        ),
    ]
