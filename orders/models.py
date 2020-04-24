from django.db import models
from menu.models import Product
from users.models import CustomUser

from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Orders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])

class Order(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    food_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # unit_price = models.ForeignKey(Orders,)
