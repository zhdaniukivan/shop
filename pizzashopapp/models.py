from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    consist_of = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='pizzashopapp/static/pizzashopapp/img/', blank=False)
    rating = models.FloatField()

    def __unicode__(self):
        return self.name

class Size(models.Model):
    SIZE_CHOICES = (
        ('option1','smol'),
        ('option2','normal'),
        ('option3','big'),
    )
    size = models.CharField(max_length=20, choices=SIZE_CHOICES)
    pizza = models.ManyToManyField(Pizza, through='PizzaSize', related_name='size')


    def __str__(self):
        return f'{self.size} - {self.pk}'

class PizzaSize(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


    class Meta(object):
        unique_together = ('pizza', 'size')

    def __str__(self):
        return f'{self.pizza}  {self.size}'


class Soup(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    consist_of = models.CharField(max_length=200)
    price = models.FloatField()
    photo = models.ImageField(upload_to='pizzashopapp/static/pizzashopapp/img/', blank=False)
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

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20)
    total_amount = models.DecimalField(auto_created=True, max_digits=10, decimal_places=2)
    order_description = models.TextField(max_length=300)


    def __str__(self):
        return self.order_number







