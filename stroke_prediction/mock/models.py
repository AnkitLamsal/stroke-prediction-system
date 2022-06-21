from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Model(models.Model):
    # Numerical value
    age = models.PositiveBigIntegerField()
    bmi = models.FloatField(validators=[MinValueValidator(0.0)])
    average_glucose_level = models.FloatField(validators=[MinValueValidator(0.0)])
    #Binary Values
    choices_ = [('yes','yes'),('no','no')]
    hypertension = models.CharField(max_length=10, choices=choices_)
    heartdisease = models.CharField(max_length=10, choices=choices_)
    martial_choice = [('married','married'),('unmarried','unmarried')]
    martial_status = models.CharField(max_length=10, choices=martial_choice)    
    residence_choice = [("urban", "urban"),("rural",'rural')]
    residence = models.CharField(max_length=10, choices=residence_choice)
    # Categorical Values
    work_choices = [('private','private'),
                    ('self','self'),
                    ('govt','govt'),
                    ('child','child'),
                    ('never_worked','never_worked')]
    work_type = models.CharField(max_length=20, choices=work_choices)
    smoking_choices = [
        ('formerly','formerly'),
        ('never','never'),
        ('smokes','smokes'),
        ('unknown','unknown')]
    smoking_status = models.CharField(max_length=20,choices=smoking_choices)
    gender_choices = [
        ('male','male'),
        ('female','female'),
        ('other','other')
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    
    prediction = models.BooleanField()
