from django.contrib import admin
from django.urls import path
from students import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user"),
    path('customer/<str:pk>/', views.customerPage, name="customer"),
    path('', views.homePage, name="home"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('products/', views.productsPage, name="products"),
    path('create-order/<str:pk>/', views.createOrder, name="create-order"),
    path('create-new-order/', views.createNewOrder, name="create-new-order"),
    path('update-order/<str:pk>/', views.updateOrder, name="update-order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
    path('create-customer/', views.createCustomer, name="create-customer"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
