# Generated by Django 4.0.5 on 2022-06-27 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_phone_student_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Info',
        ),
    ]
