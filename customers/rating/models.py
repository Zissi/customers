from django.db import models

class CustomerRating(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    rating = models.IntegerField(blank=True)
    contacted = models.BooleanField(default=False)
