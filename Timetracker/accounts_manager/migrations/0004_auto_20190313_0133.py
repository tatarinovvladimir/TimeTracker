# Generated by Django 2.1.5 on 2019-03-12 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_manager', '0003_auto_20190313_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
