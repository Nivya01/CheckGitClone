# Generated by Django 5.1.3 on 2024-11-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_theatre_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(max_length=50),
        ),
    ]