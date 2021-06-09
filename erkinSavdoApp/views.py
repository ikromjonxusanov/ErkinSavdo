from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import *
from .decorators import  *
from .filters import HomeFilter

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator

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

def explore(request):
    homes = Home.objects.order_by('-createDate')
    hFilter = HomeFilter(request.GET, queryset=homes)
    homes = hFilter.qs
    paginator = Paginator(homes, 8)
    try:
        page_number = request.GET.get('page')
    except:
        page_number = 1
    homes = paginator.get_page(page_number)

    return render(request, 'erkinSavdo/explore.html',
                  {'homes':homes, 'hFilter':hFilter})

def detailExplore(request, pk):
    home = get_object_or_404(Home, pk)

    rekHomes = []
    rekhomes = Home.objects.order_by("-createDate")
    for object in rekhomes:
        if home != object and len(rekHomes)!=4:
            rekHomes.append(object)
    return render(request, 'erkinSavdo/exploreDetail.html', {'home':home, 'rekhouses':rekHomes})

@unauthenticated
def signup(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        customerForm = CustomerForm(data=request.POST)
        if user_form.is_valid() and customerForm.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login')
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
    logout(request)
    return redirect("/")

@customer_required
def profile(request, username=None):
    try:
        if username != None:
            user = User.objects.get(username=username)
            return render(request, 'erkinSavdo/profile.html', {'user':user})
        else:
            return render(request, 'erkinSavdo/profile.html')

    except:
        return HttpResponse("404 not found")

@customer_required
def user_all_ads(request):
    return render(request, 'erkinSavdo/user-all-ads.html')

@customer_required
def addHome(request):
    form = HomeForm()
    if request.method == "POST":
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                customer = request.user.customer
                addHome = form.save(commit=False)
                addHome.author = customer
                addHome.save()
                return redirect('explore')
            except:
                return HttpResponse("Invalid user")
        return HttpResponse("Invalid Value")
    return render(request, 'home/homeForm.html', {'form':form})

@customer_required
def changeProfile(request):
    user = request.user
    customer = user.customer
    userForm = ChangeUser(instance=user)
    customerForm = CustomerForm(instance=customer)
    if request.method == "POST":
        userForm = ChangeUser(request.POST, instance=user)
        customerForm = CustomerForm(request.POST, request.FILES, instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            userForm.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('profile')
        print(userForm.is_valid() , customerForm.is_valid())
    return render(request, 'erkinSavdo/ChangeProfile.html', {'user_form':userForm, "customerForm":customerForm})

@customer_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })



