# Generated by Django 2.1.5 on 2019-04-03 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_auto_20190403_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='Author', to='accounts_manager.Profile'),
        ),
    ]
