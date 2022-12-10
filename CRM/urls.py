from django.contrib import admin
from django.urls import path
from students import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('customer/<str:pk>/', views.customerPage, name="customer"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('products/', views.productsPage, name="products"),
]
