from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import *
from .decorators import  *

# Create your views here.
def get_object_or_404(CLass, pk):
    try:
        return CLass.objects.get(id=pk)
    except:
        return HttpResponse("404 not found")

def home(request):
    queryset = Home.objects.order_by('-createDate')
    homes = []
    for object in queryset:
        if len(homes) != 4:
            homes.append(object)
    return render(request, 'erkinSavdo/index.html', {'homes':homes})

def houses(request):
    homes = Home.objects.order_by('-createDate')
    return render(request, 'erkinSavdo/properties.html', {'homes':homes})

def house(request, pk):
    home = get_object_or_404(Home, pk)
    rekHomes = []
    rekhomes = Home.objects.order_by("-createDate")
    for object in rekhomes:
        if home != object and len(rekHomes)!=4:
            rekHomes.append(object)
    return render(request, 'erkinSavdo/propertie.html', {'home':home, 'rekhouses':rekHomes})

def signup(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        customerForm = CustomerForm(data=request.POST)
        if 0  == len(request.POST['password']):
            messages.info(request, "Enter the password!")
        elif len(request.POST['password']) < 8:
            messages.info(request, "Password min length 8")
        if user_form.is_valid() and customerForm.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
        else:
            messages.info(request, user_form.errors)
    else:
        user_form = UserForm()
        customerForm = CustomerForm()
    return render(request, 'registration/registration.html',
                  context={'user_form': user_form, "customerForm": customerForm, "registered": registered})

@unauthenticated
def user_login(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    error = 'Disabled account'
            else:
                error = 'Invalid login'
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {'form': form, "error":error})

@login_required
def user_logout(request):
    try:
        del request.session['username']
    except:
        pass
    logout(request)
    return redirect("/")
