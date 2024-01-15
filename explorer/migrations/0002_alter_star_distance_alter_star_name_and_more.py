# Generated by Django 5.0.1 on 2024-01-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='distance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='star',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='star',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='starsystem',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
