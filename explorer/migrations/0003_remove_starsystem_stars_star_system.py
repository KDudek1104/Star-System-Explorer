# Generated by Django 5.0.1 on 2024-01-14 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0002_alter_star_distance_alter_star_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='starsystem',
            name='stars',
        ),
        migrations.AddField(
            model_name='star',
            name='system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='explorer.starsystem'),
        ),
    ]
