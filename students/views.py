from django.shortcuts import render

# Create your views here.


def homePage(request):
    return render(request, 'home.html')

def customerPage(request):
    return render(request, 'customer.html')