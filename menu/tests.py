from django.test import TestCase, SimpleTestCase
from .models import Product, Toppings
from django.urls import reverse
from django.contrib.auth import get_user_model
from users.models import CustomUser

# Create your tests here.
class ProductModelTest(TestCase):

    def setUp(self):
        Product.objects.create(
            title='Pancakes',
            size='Large',
            unit_price = 3.5,
            item_category = 'Desserts',
            number_of_toppings = 1
        )
    
    def test_product_object(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.title}'
        self.assertEqual(f'{product.title}', 'Pancakes')
        self.assertEqual(f'{product.size}', 'Large')
        self.assertEqual(f'{product.unit_price}', '3.5')
        self.assertEqual(f'{product.item_category}', 'Desserts')
        self.assertEqual(f'{product.number_of_toppings}', '1')


class ToppingsModelTest(TestCase):

    def setUp(self):
        Toppings.objects.create(
            title = 'Maple syrup',
            unit_price = 0.5,
            item_category = 'Desserts',
        )
    
    def test_toppings_object(self):
        topping = Toppings.objects.get(id=1)        
        self.assertEqual(f'{topping.title}', 'Maple syrup')
        self.assertEqual(f'{topping.unit_price}', '0.5')
        self.assertEqual(f'{topping.item_category}', 'Desserts')

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/') 
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self): 
        response = self.client.get(reverse('home')) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'main_list.html')

class SignupPageTest(TestCase):

    username = 'testuser',
    email = 'testuser@test.com',
    first_name = 'Test',
    last_name = 'User',
    city = 'TestTown'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup')) 
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup')) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_signup_form(self):
        new_user = CustomUser.objects.create(
            username = self.username,
            email = self.email, 
            first_name = self.first_name, 
            last_name = self.last_name, 
            city = self.city
             )

        self.assertEqual(get_user_model().objects.all().count(), 1) 
        self.assertEqual(get_user_model().objects.all()[0].username, f'{self.username}') 
        self.assertEqual(get_user_model().objects.all()[0].email, f'{self.email}')
        self.assertEqual(get_user_model().objects.all()[0].first_name, f'{self.first_name}')
        self.assertEqual(get_user_model().objects.all()[0].last_name, f'{self.last_name}')
        self.assertEqual(get_user_model().objects.all()[0].city, f'{self.city}')

class ItemPageTest(TestCase):

    def setUp(self):
        Product.objects.create(
            title='Pancakes',
            size='Large',
            unit_price = 3.5,
            item_category = 'Desserts',
            number_of_toppings = 1
        )
        Toppings.objects.create(
            title = 'Maple syrup',
            unit_price = 0.5,
            item_category = 'Desserts',
        )

    def test_item_page_status_code(self):
        product = Product.objects.get(id=1)
        response = self.client.get(f'/{product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_item_page_view_url_by_name(self):
        product = Product.objects.get(id=1)
        response = self.client.get(reverse('item_detail', kwargs={'pk':product.id})) 
        self.assertEqual(response.status_code, 200)

    def test_item_page_view_uses_correct_template(self):
        product = Product.objects.get(id=1)
        response = self.client.get(reverse('item_detail', kwargs={'pk':product.id})) 
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'item.html')
    
    def test_toppings_for_product(self):
        product = Product.objects.get(id=1)
        topping = Toppings.objects.get(id=1)
        response = self.client.get(reverse('item_detail', kwargs={'pk':product.id}))
        self.assertEqual(f'{product.number_of_toppings}', '1')


# kaip patikrinti jog rodo tuos toppingus, kokius turi rodyti?
