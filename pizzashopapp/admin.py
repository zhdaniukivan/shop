from django.contrib import admin
from .models import Pizza, Soup, Other, Order, Size, PizzaSize

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Soup)
admin.site.register(Other)
admin.site.register(Order)
admin.site.register(Size)
admin.site.register(PizzaSize)
