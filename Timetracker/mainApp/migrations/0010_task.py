# Generated by Django 2.1.5 on 2019-03-18 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_manager', '0003_remove_profile_alowed_projects'),
        ('mainApp', '0009_auto_20190317_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=400)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('t_type', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('estimated_time', models.FloatField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_manager.Profile')),
                ('performers', models.ManyToManyField(related_name='performers', to='mainApp.Project')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='mainApp.Project')),
            ],
        ),
    ]
