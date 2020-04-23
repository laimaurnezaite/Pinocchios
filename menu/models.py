from django.db import models

# Create your models here.
class MainDish(models.Model):
    title = models.CharField(max_length = 255)
    size = models.CharField(max_length = 5, blank=True)
    unit_price = models.FloatField()
    item_category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class FreeToppings(models.Model):
    title = models.CharField(max_length = 255)
    item_category = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Toppings(models.Model):
    title = models.CharField(max_length = 255)
    unit_price = models.FloatField()
    item_category = models.CharField(max_length=255)

    def __str__(self):
        return self.title