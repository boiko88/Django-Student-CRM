from django.shortcuts import render
from .models import *

# Create your views here.


def homePage(request):
    return render(request, 'home.html')


def customerPage(request):
    return render(request, 'customer.html')


def dashboardPage(request):
    return render(request, 'dashboard.html')


def productsPage(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

