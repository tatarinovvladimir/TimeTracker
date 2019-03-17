# Generated by Django 2.1.5 on 2019-03-14 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20190309_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Author', to='accounts_manager.Profile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_developer',
            field=models.ManyToManyField(related_name='Developers', to='accounts_manager.Profile'),
        ),
    ]
