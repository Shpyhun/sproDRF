from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Store(models.Model):
    """Model representing an author"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    owner = models.ForeignKey('auth.User', related_name='stores', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        choices=(
            ('active', 'Active'),
            ('deactivated', 'Deactivated'),
            ('in_review', 'In_review'),
        ),
        max_length=20,
        default='in_review'
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']



