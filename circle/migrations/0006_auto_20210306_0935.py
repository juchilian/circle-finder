# Generated by Django 2.2 on 2021-03-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0005_circle_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='スラッグ'),
        ),
    ]