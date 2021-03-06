# Generated by Django 3.2.5 on 2022-06-21 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='average_glucose_level',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='model',
            name='bmi',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]
