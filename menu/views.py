from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product, Toppings


# Create your views here.

def menu_list(request):
    menu_items = Product.objects.all()
    menu_categories = []
    for item in menu_items:
        if item.unit_price == 0.0 or item.unit_price == 0.5:
            continue
        if item.item_category not in menu_categories:
            menu_categories.append(item.item_category)

    context = {
            'menu_categories':menu_categories,
            'menu_items':menu_items

        }
    return render(request, 'main_list.html', context)

def menu_item(request, pk):
    product = Product.objects.get(id=pk)
    toppings = ''
    if product.number_of_toppings > 0:
        if product.item_category == "Regular Pizza" or product.item_category == "Sicilian Pizza":
            toppings = Toppings.objects.filter(item_category="Pizza")
        else:
            toppings = Toppings.objects.filter(item_category="Subs")
    
    number_of_toppings = product.number_of_toppings
    context = {
            'product':product,
            'toppings':toppings,
            'number_of_toppings':number_of_toppings,

        } 
    return render(request, 'item.html', context)