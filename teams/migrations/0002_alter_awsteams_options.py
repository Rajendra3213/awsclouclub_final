# Generated by Django 5.0.6 on 2024-07-24 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awsteams',
            options={'verbose_name': 'AWS Team', 'verbose_name_plural': 'AWS Teams'},
        ),
    ]