from django.db import models
import joblib

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
        ('mild','Mild'),
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

    min_ph=models.FloatField()
    max_ph=models.FloatField()
    min_precipitation=models.FloatField()
    max_precipitation=models.FloatField()
    duration=models.CharField(max_length=20,blank=True,null=True,choices=DURATION_CHOICES,default='annual')
    growth_habit=models.CharField(max_length=20,blank=True,null=True,choices=GROWTH_HABIT_CHOICES,default='forb/herb')
    soil_texture=models.CharField(max_length=10,choices=TEXTURE_CHOICES,default='coarse')
    min_temperature=models.FloatField()
    shade_tolerance=models.CharField(max_length=20,choices=SHADE_CHOICES,default='Intermediate')
    drought_tolerance=models.CharField(max_length=20,choices=DROUGHT_CHOICES,default='Low')
    prediction=models.CharField(max_length=200,editable=False,blank=True,null=True)

    def __str__(self):
        return 'Predicted: '+self.prediction

    def save(self,*args,**kwargs):
        try:
            #loaded_model=joblib.load('./trained_model/dtreev1.sav')
            #prediction=loaded_model.predict([[self.]])
            self.prediction='grass' #for now
        except:
            pass
        super().save(*args,**kwargs)