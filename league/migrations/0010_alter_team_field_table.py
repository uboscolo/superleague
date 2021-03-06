# Generated by Django 4.0 on 2021-12-19 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0009_tier_playoff_series_tier_relegations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='field',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='league.venue'),
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='league.tier')),
            ],
        ),
    ]
