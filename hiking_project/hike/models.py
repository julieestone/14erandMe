from django.conf import settings
from django.db import models

# Create your models here.
    
class Trail(models.Model):
    hike_name = models.CharField(max_length=200)
    hike_location = models.CharField(max_length=200)
    hike_city = models.CharField(max_length=100)
    hike_difficulty = models.CharField(max_length=20)
    hike_milage = models.DecimalField(max_digits=2, decimal_places=1)
    hike_description = models.TextField()
    hike_image_file = models.FileField(null=True, blank=True)
    hike_image = models.TextField(null=True, blank=True)
    
    def __str__ (self):
        return f"{self.hike_name}"
    
class Review(models.Model):
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE, related_name="reviews")
    difficulty = models.CharField(max_length=20)
    review = models.TextField()
    username = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return f"id={self.id}, difficulty={self.difficulty}, review={self.review}, username={self.username}, created_date={self.created_date}"
    
    
