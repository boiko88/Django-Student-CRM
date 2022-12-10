from django.shortcuts import render
from .models import *


def homePage(request):
    return render(request, 'dashboard.html')


def dashboardPage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers,
               'total_customers': total_customers,
               'total_orders': total_orders,
               'delivered': delivered,
               'pending': pending,
               }
    return render(request, 'dashboard.html', context)
    


def productsPage(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def customerPage(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders}
    
    
    

    
    return render(request, 'customer.html', context)


