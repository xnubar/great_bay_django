from django.shortcuts import render, redirect
from .models import Customer
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User

def logout_view(request):
    logout(request)
    return redirect("login")

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name","")
        last_name = request.POST.get("last_name","")
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user_type = request.POST.get("user_type")
        customer = Customer(first_name=first_name, last_name=last_name, 
        username = username, password=password, user_type = user_type)
        customer.save()
        if customer.id:
            return render(request, "login.html")
        
    return render(request, "signup.html")

@login_required(login_url=reverse_lazy('login'))
def homepage(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user = Customer.objects.get(username=request.user)
    context = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name
    }
    if user.user_type == Customer.CUSTOMER_TYPE_CONSUMER:
        return render(request, "consumer_profile.html",context = context)
    return render(request, "owner_profile.html", context=context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == 'POST':
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = authenticate(username=username, password = password)
        if user is not  None:
            login(request, user)
           
            return redirect("homepage")
    return render(request,"login.html")


def consumer_view(request):
    pass



def owner_view(request):
    pass


        