from django.contrib import admin

from .models import Product, Toppings
# Register your models here.

admin.site.register(Product)
admin.site.register(Toppings)
