from django.shortcuts import render
from .models import *

# Create your views here.


def homePage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    context = {'orders': orders, 'customers': customers}
    
    return render(request, 'dashboard.html', context)


def customerPage(request):
    return render(request, 'customer.html')


def dashboardPage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    context = {'orders': orders, 'customers': customers}
    
    return render(request, 'dashboard.html', context)


def productsPage(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

