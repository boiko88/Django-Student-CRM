from django.http import HttpResponse
from django.shortcuts import redirect


# view_funct is executed if user is not authenticated
def unauthenticated_user(view_funcion):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return (view_funcion(request, *args, **kwargs))
    return wrapper_function


# grou is empty by default and it's checked and has data the name of the first
# one is taken. It's going to be customer and admin so far.
def allowed_users(allowed_roles=[]):
    def decorator(view_fucnion):
        def wrapper_function(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_fucnion(request, *args, **kwargs)
            else:
                return HttpResponse('You are not allowed to view this page')
        return wrapper_function
    return decorator
