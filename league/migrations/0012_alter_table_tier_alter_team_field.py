# Generated by Django 4.0 on 2021-12-19 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0011_alter_table_tier_alter_team_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.tier'),
        ),
        migrations.AlterField(
            model_name='team',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='league.venue'),
        ),
    ]
