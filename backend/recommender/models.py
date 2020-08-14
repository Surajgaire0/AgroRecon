from django.db import models
import joblib

# Create your models here.
class Plant_Recommend(models.Model):
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

    TEX_SOIL_CHOICES=(
        ('yes','Yes'),
        ('no','No')
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
    maximim_precipitation=models.FloatField()
    duration=models.CharField(max_length=20,blank=True,null=True,choices=DURATION_CHOICES,default='annual')
    growth_habit=models.CharField(max_length=20,blank=True,null=True,choices=GROWTH_HABIT_CHOICES,default='forb/herb')
    coarse_tex_soils=models.CharField(max_length=10,choices=TEX_SOIL_CHOICES,default='yes')
    medium_tex_soils=models.CharField(max_length=10,choices=TEX_SOIL_CHOICES,default='no')
    fine_tex_soils=models.CharField(max_length=10,choices=TEX_SOIL_CHOICES,default='no')
    min_tempearature=models.FloatField()
    shade_tolerance=models.CharField(max_length=20,choices=SHADE_CHOICES,default='Intermediate')
    drought_tolerance=models.CharField(max_length=20,choices=DROUGHT_CHOICES,default='Low')
    prediction=models.CharField(max_length=200,blank=True,null=True)

    # def save(self,*args,**kwargs):
    #     try:
    #         loaded_model=joblib.load('./trained_model/dtreev1.sav')
    #         prediction=loaded_model.predict([[self.]])
            