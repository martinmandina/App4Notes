# Generated by Django 3.1.3 on 2020-12-10 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='createdtime',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='notes',
            old_name='modifiedtime',
            new_name='modified_at',
        ),
    ]
