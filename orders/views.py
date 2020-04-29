from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView

from django.contrib.auth import get_user_model
from .models import Order#, ShoppingCart
from menu.models import Product
from users.models import CustomUser

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

class OrderDetail(ListView):
    model = Order
    template_name = 'order_detail.html'
    
def shopping_cart(request):
    customer_id = int(request.user.id)
    customer = CustomUser.objects.filter(id=customer_id)
    if request.method == "POST":
        quantity = float(request.POST.get('quantity'))
        product_id = int(request.POST.get('product'))
        product = Product.objects.filter(id=product_id)
        for data in product:
            sum = round(quantity * data.unit_price, 2)

        new_order = Order()
        new_order.items = {
            "product_id":request.POST.get('product'),
            "quantity":quantity}
        new_order.customer_id = customer_id
        new_order.sum = sum
        new_order.save()
        context = {
            'order':new_order,
            'customer':customer,
            'product' : product,
        }
        return render(request, 'shopping_cart.html', context)
    else:
        open_orders = Order.objects.filter(customer_id=customer_id, confirmed = False)
        print("-------")
        for order in open_orders:
            print(order.date)
        # print(open_orders)
        for data in open_orders:
            product = Product.objects.filter(id=data.items['product_id'])
        context = {
            'customer':customer,
            'order':open_orders,
            'product':product,
        }
    return render(request, 'shopping_cart.html', context)

def confirmOrder(request):

    if request.POST:

        order_id = request.POST.get('order_id')
        order_to_confirm = Order.objects.get(id=order_id)
        order_to_confirm.confirmed = True
        order_to_confirm.save()

    return redirect ('/')

def confirmed_orders(request):
    customer_id = int(request.user.id)
    customer = CustomUser.objects.filter(id=4)    
    orders = Order.objects.filter(customer_id=customer_id, confirmed = True)
    print(orders) 
    customer = CustomUser.objects.filter(id=customer_id)
    product = ''
    for data in orders:
            product = Product.objects.filter(id=data.items['product_id'])
    print("CUSTOMER")
    # print(orders.items)
    context = {
            'customer':customer,
            'order':orders,
            'product':product
        }
    return render(request, 'confirmed.html', context)
