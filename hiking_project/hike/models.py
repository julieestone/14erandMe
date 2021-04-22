from django.conf import settings
from django.db import models

# Create your models here.
    
class Trail(models.Model):
    hike_name = models.CharField(max_length=200)
    hike_location = models.CharField(max_length=200)
    hike_difficulty = models.CharField(max_length=20)
    hike_milage = models.DecimalField(max_digits=2, decimal_places=1)
    hike_description = models.CharField(max_length=1000)
    
    def __str__ (self):
        return f"id={self.id}, hike_name={self.hike_name}, hike_location={self.hike_location}, hike_difficulty={self.hike_difficulty}, hike_milage={self.hike_milage}, hike_description={self.hike_description}"
    
class Review(models.Model):
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name="reviews")
    difficulty = models.CharField(max_length=20)
    review = models.CharField(max_length=2000)
    username = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"id={self.id}, difficulty={self.difficulty}, review={self.review}, username={self.username}, created_date={self.created_date}"
    
    
