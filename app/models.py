from django.db import models

# Create your models here.
class City(models.Model):
    city=models.CharField(max_length=100)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)

class SunSet(models.Model):
    city = models.ForeignKey(City, related_name='sun_set', on_delete=models.CASCADE)
    name = models.TextField(max_length=500)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    photos=models.TextField(max_length=100)
    review_score=models.TextField(max_length=20,null=True)
    hours=models.TextField(max_length=150,null=True)
    address=models.TextField(max_length=100,null=True)
    tips=models.TextField(max_length=3000,null=True)