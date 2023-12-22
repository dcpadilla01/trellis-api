from django.db import models

# Create your models here.
class Conversions(models.Model):
    original_number = models.IntegerField()
    converted_number = models.TextField()