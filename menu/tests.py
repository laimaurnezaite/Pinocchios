from django.test import TestCase
from .models import Product, Toppings

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

    