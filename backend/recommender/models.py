import json
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from .predict import predict

# Create your models here.
class Recommend(models.Model):
    DURATION_CHOICES=(
        ('perennial','Perennial'),
        ('annual','Annual'),
        ('biennial','Biennial')
    )

    GROWTH_HABIT_CHOICES=(
        ('shrub','Shrub'),
        ('forb/herb','Forb/Herb'),
        ('graminoid','Graminoid'),
        ('subshrub','Subshrub'),
        ('tree','Tree'),
        ('vine','Vine')
    )

    TEXTURE_CHOICES=(
        ('coarse','Coarse'),
        ('medium','Medium'),
        ('fine','Fine')
    )

    SHADE_CHOICES=(
        ('intolerant','Intolerant'),
        ('intermediate','Intermediate'),
        ('tolerant','Tolerant')
    )

    DROUGHT_CHOICES=(
        ('none','None'),
        ('low','Low'),
        ('medium','Medium'),
        ('high','High')
    )

    ph=models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(14)])
    min_precipitation=models.FloatField()
    max_precipitation=models.FloatField()
    duration=models.CharField(max_length=20,blank=True,null=True,choices=DURATION_CHOICES,default='annual')
    growth_habit=models.CharField(max_length=20,blank=True,null=True,choices=GROWTH_HABIT_CHOICES,default='forb/herb')
    soil_texture=models.CharField(max_length=10,choices=TEXTURE_CHOICES,default='coarse')
    min_temperature=models.FloatField()
    shade_tolerance=models.CharField(max_length=20,choices=SHADE_CHOICES,default='Intermediate')
    drought_tolerance=models.CharField(max_length=20,choices=DROUGHT_CHOICES,default='Low')
    prediction=models.CharField(max_length=300,editable=False,blank=True,null=True)

    def __str__(self):
        return 'Prediction: '+str(self.id)

    def save(self,*args,**kwargs):
        try:
            self.prediction=json.dumps(predict(self.min_temperature,self.max_precipitation,self.min_precipitation,self.ph,self.shade_tolerance,self.drought_tolerance,self.soil_texture))
            super().save(*args,**kwargs)
        except Exception as e:
            print (e)


