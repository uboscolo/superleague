# Generated by Django 4.0 on 2021-12-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0027_league_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='home_factor',
            field=models.DecimalField(decimal_places=1, default=1.5, max_digits=2),
        ),
        migrations.AddField(
            model_name='match',
            name='luck_factor',
            field=models.DecimalField(decimal_places=1, default=2.0, max_digits=2),
        ),
    ]
