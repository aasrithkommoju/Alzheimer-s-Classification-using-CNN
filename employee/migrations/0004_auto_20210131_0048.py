# Generated by Django 3.0.3 on 2021-01-30 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20201210_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='UPLOAD_LEAF_IMAGE',
            new_name='UPLOAD_MRI_IMAGE',
        ),
    ]
