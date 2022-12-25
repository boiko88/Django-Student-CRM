from django.contrib import admin
from django.urls import path
from students import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user"),
    path('user-settings/', views.userSettings, name="user-settings"),
    path('customer/<str:pk>/', views.customerPage, name="customer"),
    path('', views.homePage, name="home"),
    path('dashboard/', views.dashboardPage, name="dashboard"),
    path('products/', views.productsPage, name="products"),
    path('create-order/<str:pk>/', views.createOrder, name="create-order"),
    path('create-new-order/', views.createNewOrder, name="create-new-order"),
    path('update-order/<str:pk>/', views.updateOrder, name="update-order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
    path('create-customer/', views.createCustomer, name="create-customer"),
    
    # Lower auth_views method is used to deal with password restorage
    #<uidb64>/<token> these come from the documentations for auth_views
    path('reset-password/', auth_views.PasswordResetView.as_view(), name="reset-password"),
    path('reset-password-sent/', auth_views.PasswordResetDoneView.as_view(), name="reset-password-sent"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="reset-password-complete"),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name="reset-password-complete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
