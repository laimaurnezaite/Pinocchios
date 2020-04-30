from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 255)
    size = models.CharField(max_length = 5)
    unit_price = models.FloatField(null=True, blank=True)
    item_category = models.CharField(max_length=255)
    number_of_toppings = models.IntegerField(default=0)

    def __str__(self):
        return self.title
class Toppings(models.Model):
    title = models.CharField(max_length = 255)
    unit_price = models.FloatField(null=True, blank=True)
    item_category = models.CharField(max_length=255)

    def __str__(self):
        return self.title