from django.db import models

# Create your models here.


class Coffe(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    consist = models.TextField()
    img = models.ImageField()


class Publication(models.Model):
    title = models.CharField(max_length=111)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateField()


class Comment(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField()
    date = models.DateField(null=True)



