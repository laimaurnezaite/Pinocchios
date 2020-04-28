from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from django.contrib.auth import get_user_model
from .models import Order
from menu.models import Product
from users.models import CustomUser

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

class OrderDetail(ListView):
    model = Order 
    template_name = 'order_detail.html'


    
def AddToOrder(request):
    if request.method == "POST":
        quantity = float(request.POST.get('quantity'))
        product_id = int(request.POST.get('product'))
        customer_id = int(request.user.id)

        product = Product.objects.filter(id=product_id)
        for data in product:
            sum = round(quantity * data.unit_price, 2)

        customer = CustomUser.objects.filter(id=customer_id)
        context = {
            'quantity': quantity,
            'customer':customer,
            'product' : product,
            'sum': sum,
        }
        return render(request, 'order_detail.html', context)
        # return HttpResponse("Project 3: TODO")
    # else:
    #     return HttpResponse("Project 3: ")
        # if request.POST.get('quantity'):
        #     print("TEST TEST TEST")
        #     quantity = request.POST.get('quantity')
        #     customer_id = request.user.id
        #     title=request.POST.get(object.title)
        #     print(title)
        #     product_id = request.POST.get(object.title)
        #     order = Order(customer_id = customer_id, product_id=product_id)
        #     # order.customer_id = request.user
            
        #     # print(current_user)
        #     # order = Order()
        #     order.quantity = int(request.POST.get('quantity'))
        #     order.save()
        #     return HttpResponse("Project 3: TODO")
        # else:
        #     return render(request, 'order_detail.html')

def confirmOrder(request):

    if request.POST:
        confirmed_order = Order()
        confirmed_order.product_id = request.POST.get('product')
        confirmed_order.quantity = int(float(request.POST.get('quantity')))
        # quantity = int(float(request.POST.get('quantity')))
        # quantity2=int(quantity)
        # print("aaaaaaaaaasaaaaaaaaaa")
        # print(type(quantity))
        confirmed_order.customer_id = request.POST.get('customer')
        confirmed_order.save()
        return HttpResponse("Order confirmed!")

