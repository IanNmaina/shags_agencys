# Generated by Django 5.0.4 on 2024-04-24 11:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties_for_rent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='AvailableBy',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
