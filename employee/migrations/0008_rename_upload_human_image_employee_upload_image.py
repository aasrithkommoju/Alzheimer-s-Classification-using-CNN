# Generated by Django 3.2.7 on 2021-09-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20210914_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='UPLOAD_HUMAN_IMAGE',
            new_name='UPLOAD_IMAGE',
        ),
    ]
