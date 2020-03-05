from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.decorators import login_required
from Sale.models import Order_Product
from Management.models import Product, Order, Type


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

def Index(request, key_of=0):
    product = Product.objects.all().order_by('pk')
    cart, alert = {}, ''
    
    if request.method == 'POST':
        item = Product.objects.get(name__iexact=request.POST.get('get_product'))
        amount = int(request.POST.get('amount'))
        not_send = ''
        
        if amount > item.storage:
            alert = 'In Storage have ' + str(item.storage)
            not_send = request.POST.get('not_send')
            amount = 0
        
        # Deduct item in storage
        item.storage -= amount
        item.save()
        
        # Delete
        if item.storage <= 0:
            item.delete()
        
        #create order
        o = Order(id_of_order='23233', total_price=item.price*amount)
        o.save()
        
        order_product = Order_Product(order_id=o, product_id=item, amount=amount)
        order_product.save()
        
        
        cart = {
            'name': item.name,
            'type': item.type_of,
            'price': item.price * amount if amount != 0 else 1,
            'amount': amount,
            'not_send': not_send
        }
    
    return render(request, 'index/index.html', context = {
        'product': product,
        'alert': alert,
        'name': request.user.username,
        'cart': cart,
        'number_counter': key_of 
    })

    
def random():
    listed_of_number = [[0, 1, 2], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number_random = ''
    
    for rb in listed_of_number[0]:
        number_random += str(rb)
        
    return number_random
    