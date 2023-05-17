from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    consist_of = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='pizzashopapp_photo_pizza/', blank=False)
    rating = models.FloatField()
    def __str__(self):
        return self.name

class Soup(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    consist_of = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='pizzashopapp_photo_soup/', blank=False)
    rating = models.FloatField()
    def __str__(self):
        return self.name


class Water(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    consist_of = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='pizzashopapp_photo_water/', blank=False)
    rating = models.FloatField()
    def __str__(self):
        return self.name


class Other(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    consist_of = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='pizzashopapp_pthoto_ather/', blank=False)
    rating = models.FloatField()

    def __str__(self):
        return self.name







