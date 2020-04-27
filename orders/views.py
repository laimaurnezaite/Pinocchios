from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Order

# Create your views here.
def index(request):
    return HttpResponse("Project 3: TODO")

class OrderDetail(ListView):
    model = Order 
    template_name = 'order_detail.html'

class AddToOrderView(CreateView):
    model = Order
    template_name = 'order_detail.html'
    fields = ('quantity',)