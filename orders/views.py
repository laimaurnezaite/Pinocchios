from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView

from django.contrib.auth import get_user_model
from .models import Order#, ShoppingCart
from menu.models import Product, Toppings
from users.models import CustomUser

# helper functions

def get_customer_object(request):
    customer_id = int(request.user.id)
    customer = CustomUser.objects.filter(id=customer_id)
    return customer

def get_customer_id(request):
    customer_id = int(request.user.id)
    return customer_id

def get_order(customer_id, confirmed):
    order = Order.objects.get(customer_id=customer_id, confirmed = confirmed)
    return order

def filter_order(customer_id, confirmed):
    orders = Order.objects.filter(customer_id=customer_id, confirmed = confirmed)
    return orders

# Create your views here.
# def index(request):
#     return HttpResponse("Project 3: TODO")

def add(request):
    # get information from POST request about customer and retrieve information about customer from database
    customer = get_customer_object(request)
    customer_id = get_customer_id(request)

    # get product ID, quantity and toppings from POST request, get product object from database 
    quantity = float(request.POST.get('quantity'))
    product_id = int(request.POST.get('product'))
    product = Product.objects.get(id=product_id)
    sum = round(quantity * product.unit_price, 2)
    toppings_ids = request.POST.getlist('toppings')
    list_of_toppings = []

    if toppings_ids == None:
        topping = ''
        sum = round(quantity * product.unit_price, 2)
    else: 
        for topping_id in toppings_ids:
            topping = Toppings.objects.get(id=topping_id)
            list_of_toppings.append(topping.title)
            sum = round(quantity * product.unit_price, 2) + round(quantity * topping.unit_price, 2)

    # try to reach currently open orders and append it, if not - create new one
    try:
        open_order = get_order(customer_id, False)

        if request.method == "POST":
            open_order.items.append({
                "product_id":product_id,
                "product_title":product.title,
                "quantity":quantity,
                "price": product.unit_price,
                "sum": sum,
                "category": product.item_category, 
                "size":product.size,
                'toppings':list_of_toppings})
            open_order.total = round(open_order.total + sum, 2)
            open_order.save() 

            context = {
                'order':open_order,
                'customer':customer,
                }
            
            return render(request, 'shopping_cart.html', context)           
    except:
        if request.method == "POST":
            new_order = Order()
            new_order.items = [{
                "product_id":product_id,
                "product_title":product.title,
                "quantity":quantity,
                "price": product.unit_price,
                "sum": sum,
                "category": product.item_category, 
                "size":product.size,
                'toppings':list_of_toppings}]
            new_order.customer_id = customer_id
            new_order.total = sum
            new_order.save()
        
            context = {
                'order':new_order,
                'customer':customer
            }
            return render(request, 'shopping_cart.html', context)

    
def shopping_cart(request):
    # retrieve not confirmed orders
    
    try:
        customer_id = get_customer_id(request)
        customer = get_customer_object(request)
        print("TEST1")
        print("TEST2")
        open_order = get_order(customer_id, False)
        print("TEST3")
        context = {
                'order':open_order,
                'customer':customer,
                }
        print("TEST4")
        return render(request, 'shopping_cart.html', context) 
    except:
        print("TEST5")
        context = {
            'message':"There are no items in shopping cart"
        }
        return render(request, 'apology.html', context)


def confirmOrder(request):
    # change order object field 'confirmed' value
    if request.POST:
        order_id = request.POST.get('order_id')
        order_to_confirm = Order.objects.get(id=order_id)
        order_to_confirm.confirmed = True
        order_to_confirm.save()
        customer_id = get_customer_id(request)
        customer = get_customer_object(request)
        confirmed_orders = filter_order(customer_id, True)  

        context = {
                'customer':customer,
                'order':confirmed_orders,
            }
    return render(request, 'confirmed.html', context)

def confirmed_orders(request):
    try:
        # retrieve confirmed orders
        customer_id = get_customer_id(request)
        customer = get_customer_object(request)
        confirmed_orders = filter_order(customer_id, True)
        
        context = {
                'customer':customer,
                'order':confirmed_orders,
            }
        return render(request, 'confirmed.html', context)
    except:
        context = {
            'message':"You need to be logged in to see order history."
        }
        return render(request, 'apology.html', context)