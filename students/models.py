from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated', '-date_created']
    
    def __str__(self):
        return f'{self.name}'
    

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Product(models.Model):
    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out door', 'Out door'),
            )
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category= models.CharField(max_length=50, null=True, choices=CATEGORY)
    description = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f'{self.name}'
    
    
class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out for delivery', 'Our for delivery'),
            ('Delivered', 'Delivered'),
            )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1200, null=True)
    
    def __str__(self):
        return f"{self.customer}'s Order"

    