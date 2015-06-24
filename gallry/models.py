from django.db import models

# Create your models here.

class Gallry(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)