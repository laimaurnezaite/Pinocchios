from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import CustomUser

# Create your tests here.

class CustomUserModelTest(TestCase):

    def setUp(self):
        CustomUser.objects.create(
            username = 'testuser',
            email = 'testuser@test.com',
            first_name = 'Test',
            last_name = 'User',
            city = 'TestTown'
        )
    
    def test_user_object(self):
        user = CustomUser.objects.get(id=1)        
        self.assertEqual(f'{user.username}', 'testuser')
        self.assertEqual(f'{user.email}', 'testuser@test.com')
        self.assertEqual(f'{user.first_name}', 'Test')
        self.assertEqual(f'{user.last_name}', 'User')
        self.assertEqual(f'{user.city}', 'TestTown')

    