from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Product


# Create your views here.

# class MenuListView(ListView):
#     model = Product
#     template_name = 'main_list.html'

class MenuItemDetailView(DetailView):
    model = Product
    template_name = 'menu_item_detail.html'


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

