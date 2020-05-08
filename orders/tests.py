from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Order
from users.models import CustomUser
import unittest

# Create your tests here.

class OrderModelTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.user = CustomUser.objects.create(
            username = 'testuser',
            email = 'testuser@test.com',
            first_name = 'Test',
            last_name = 'User',
            city = 'TestTown'
        )


        Order.objects.create(
            customer = self.user,
            items = [{"product_id": 584, "product_title": "Greek Salad", "quantity": 1.0, "price": 50.0, "sum": 50.0, "category": "Dinner Platters", "size": "Small", "toppings": []}],
            total = 50.0
        )
    
    def test_order_object(self):
        order = Order.objects.get(id=1)     
        self.assertEqual(f'{order.customer.id}', '1')
        
        self.assertEqual(f'{order.items}', "[{'product_id': 584, 'product_title': 'Greek Salad', 'quantity': 1.0, 'price': 50.0, 'sum': 50.0, 'category': 'Dinner Platters', 'size': 'Small', 'toppings': []}]")
        self.assertEqual(f'{order.confirmed}', 'False')
        self.assertEqual(f'{order.total}', '50.0')


    