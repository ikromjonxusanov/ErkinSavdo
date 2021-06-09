from django.shortcuts import render, redirect



def unauthenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def login_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/")
    return wrapper_func

def customer_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
                return view_func(request, *args, **kwargs)
            except:
                return redirect("/")

        else:
            return redirect("/")
    return wrapper_func



