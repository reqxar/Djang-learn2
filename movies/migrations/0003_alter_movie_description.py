# Generated by Django 3.2.6 on 2021-08-16 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_world_premiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
