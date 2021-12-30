# Generated by Django 4.0 on 2021-12-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0022_tableentry_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='tableentry',
            options={'verbose_name_plural': 'Table entries'},
        ),
        migrations.AddField(
            model_name='table',
            name='year',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
    ]