# Generated by Django 2.1.5 on 2019-03-17 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_auto_20190317_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='full_description',
            field=models.TextField(),
        ),
    ]