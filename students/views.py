from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CustomerForm
from .filters import OrderFilter


def homePage(request):
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
    # Search Functionality
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context = {'customer': customer, 'orders': orders,
               'total_orders': total_orders, 'myFilter': myFilter}

    return render(request, 'customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('dashboard')
    
    context = {'formset': formset}
    
    return render(request, 'order_form.html', context)


def createNewOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form': form}
    
    return render(request, 'order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    context = {'form': form}
    
    # Save Order Data
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    return render(request, 'order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    context = {'item': order}
    
    if request.method == "POST":
        order.delete()
        return redirect('dashboard')
    
    return render(request, 'delete.html', context)


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form': form}
    
    return render(request, 'customer_form.html', context)
    


