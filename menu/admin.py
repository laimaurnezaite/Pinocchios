from django.contrib import admin

from .models import MainDish, FreeToppings, Toppings

# Register your models here.

admin.site.register(MainDish)
admin.site.register(FreeToppings)
admin.site.register(Toppings)