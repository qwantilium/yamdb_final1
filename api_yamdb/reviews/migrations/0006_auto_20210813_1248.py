# Generated by Django 2.2.16 on 2021-08-13 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20210813_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='descrption',
            new_name='description',
        ),
    ]
