from django.db import models
import jsonfield
from menu.models import Product
from users.models import CustomUser

from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


# class ShoppingCart(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, default = 0)
#     quantity = models.IntegerField(default = 0)
#     open = models.BooleanField(default=True)

#     def __str__(self):
#         return f" Shopping cart {self.id}"


class Order (models.Model):
    # shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, default = 0)
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = jsonfield.JSONField()
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, default = 0)
    # quantity = models.IntegerField(default = 0)
    sum = models.FloatField(default = 0)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
