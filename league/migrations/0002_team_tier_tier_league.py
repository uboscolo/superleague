# Generated by Django 4.0 on 2021-12-19 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='league.tier'),
        ),
        migrations.AddField(
            model_name='tier',
            name='league',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='league.league'),
        ),
    ]
