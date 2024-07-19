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





class Contacts(models.Model):
    numb = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()

class ClientContact(models.Model):
    phone = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()




