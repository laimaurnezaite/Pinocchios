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

class ShoppingCartTest(TestCase):

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

        Order.objects.create(
            customer = self.user,
            items = [{"product_id": 506, "product_title": "1 topping", "quantity": 2.0, "price": 13.7, "sum": 27.4, "category": "Regular Pizza", "size": "Small", "toppings": ["Sausage"]}],
            total = 27.4,
        )

    def test_shopping_cart(self):
        order = Order.objects.all()
        self.assertEqual(Order.objects.all().count(), 2) 
        self.assertEqual(Order.objects.all()[0].customer.id, 1) 
        self.assertEqual(Order.objects.all()[1].customer.id, 1)
        self.assertEqual(Order.objects.all()[0].id, 1) 
        self.assertEqual(Order.objects.all()[1].id, 2)
        self.assertEqual(Order.objects.all()[0].items, [{"product_id": 584, "product_title": "Greek Salad", "quantity": 1.0, "price": 50.0, "sum": 50.0, "category": "Dinner Platters", "size": "Small", "toppings": []}])
        self.assertEqual(Order.objects.all()[1].items, [{"product_id": 506, "product_title": "1 topping", "quantity": 2.0, "price": 13.7, "sum": 27.4, "category": "Regular Pizza", "size": "Small", "toppings": ["Sausage"]}])
        self.assertEqual(Order.objects.all()[0].total, 50.0)
        self.assertEqual(Order.objects.all()[1].total, 27.4)


class ConfirmedOrdersTest(TestCase):

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
            total = 50.0,
            confirmed = True
        )

        Order.objects.create(
            customer = self.user,
            items = [{"product_id": 506, "product_title": "1 topping", "quantity": 2.0, "price": 13.7, "sum": 27.4, "category": "Regular Pizza", "size": "Small", "toppings": ["Sausage"]}],
            total = 27.4,
            confirmed = True
        )

    def test_order_history(self):
        order = Order.objects.filter(confirmed = True)
        self.assertEqual(Order.objects.filter(confirmed = True).count(), 2)
    