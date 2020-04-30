from django.db import models
import jsonfield
from menu.models import Product
from users.models import CustomUser

from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Order (models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = jsonfield.JSONField()
    total = models.FloatField(default = 0)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('order_detail', args=[str(self.id)])
