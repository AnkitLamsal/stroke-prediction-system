# Generated by Django 3.2.5 on 2022-06-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveBigIntegerField()),
                ('bmi', models.FloatField()),
                ('average_glucose_level', models.FloatField()),
                ('hypertension', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('heartdisease', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('martial_status', models.CharField(choices=[('married', 'married'), ('unmarried', 'unmarried')], max_length=10)),
                ('residence', models.CharField(choices=[('urban', 'urban'), ('rural', 'rural')], max_length=10)),
                ('work_type', models.CharField(choices=[('private', 'private'), ('self', 'self'), ('govt', 'govt'), ('child', 'child'), ('never_worked', 'never_worked')], max_length=20)),
                ('smoking_status', models.CharField(choices=[('formerly', 'formerly'), ('never', 'never'), ('smokes', 'smokes'), ('unknown', 'unknown')], max_length=20)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=10)),
                ('prediction', models.BooleanField()),
            ],
        ),
    ]