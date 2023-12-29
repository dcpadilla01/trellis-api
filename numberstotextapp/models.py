from django.db import models


class Conversions(models.Model):
    original_number = models.IntegerField()
    converted_number = models.TextField()