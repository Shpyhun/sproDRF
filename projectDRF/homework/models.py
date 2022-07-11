from django.db import models

# Create your models here.


class Store(models.Model):
    """Model representing an author"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    rating = models.IntegerField(max_value=100, min_value=1)
