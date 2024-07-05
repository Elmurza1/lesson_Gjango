from django.db import models

# Create your models here.


class Coffe(models.Model):
    name = models.CharField(max_length=150)

    price = models.FloatField()
    consist = models.TextField()

    img = models.ImageField()
