from django.db import models
from menu.models import Product
from users.models import CustomUser

from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Order (models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
