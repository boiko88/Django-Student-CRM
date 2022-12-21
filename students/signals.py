from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer

# Signals connect users and Customers together after they are created via 
# Register Account funtionality on the page. Earlier, you had to create it by 
# admin panel only.
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile Created')


post_save.connect(customer_profile, sender=User)
