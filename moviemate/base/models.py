from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MovieGoer(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(null=False, default=False)

class MoviePreferences(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, null=False)
    movie_name = models.CharField(max_length=255, null=False)
    date =  models.DateTimeField(blank=False, null=False)
    number_of_seats = models.IntegerField(null=False)
    time_from = models.IntegerField(null=False)
    time_to = models.IntegerField(null=False)
    is_processed = models.BooleanField(null=False, default=False)
    
class SeatPreferences(models.Model):
    preference_id = models.ForeignKey(MoviePreferences,  on_delete=models.CASCADE)
    number_of_rows = models.IntegerField(null=False)
    side = models.IntegerField(null=False)
    movie_name = models.CharField(max_length=255, null=False)
    is_included = models.BooleanField(null=False, default=False)