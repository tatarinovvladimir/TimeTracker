# Generated by Django 2.1.5 on 2019-03-14 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20190314_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_developer',
            new_name='developers',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='name',
        ),
    ]