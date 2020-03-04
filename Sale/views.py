from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.decorators import login_required
from Sale.models import Order_Product
from Management.models import Product

# Login

def Login(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))

        if user:
            login(request, user)
            return redirect('/index/')

    return render(request, 'login/login.html')

@login_required
def index(request):
    return render(request, 'index/index.html', context = {'name': request.user.username})


def Logout(request):
    logout(request)
    return redirect('/login')

def go_login(request):
    return redirect('login/')


# Home

def showProduct(request):
    product = Product.objects.all()
    
    if request.method == 'POST':
        print(request)
    
    return render(request, 'index/index.html', context = {
        'product': product,
        'name': request.user.username
    })
    

    
