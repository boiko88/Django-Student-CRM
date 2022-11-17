from django.contrib import admin
from django.urls import path, include
from students import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name="home"),
]
