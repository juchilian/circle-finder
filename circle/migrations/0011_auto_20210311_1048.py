# Generated by Django 2.2 on 2021-03-11 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circle', '0010_auto_20210307_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='circle',
            name='line_url',
            field=models.URLField(blank=True, null=True, verbose_name='Line'),
        ),
        migrations.AlterField(
            model_name='circle',
            name='gender_rate',
            field=models.IntegerField(blank=True, choices=[(0, '0%'), (1, '10%'), (2, '20%'), (3, '30%'), (4, '40%'), (50, '50%'), (6, '60%'), (7, '70%'), (8, '80%'), (9, '90%'), (10, '100%')], null=True, verbose_name='男女比率'),
        ),
    ]