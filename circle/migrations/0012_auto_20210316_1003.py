# Generated by Django 2.2 on 2021-03-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0011_auto_20210311_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circle',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='アピールポイント'),
        ),
    ]
