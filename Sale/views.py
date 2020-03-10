from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.decorators import login_required
from Sale.models import Order_Product, Order_Product_Storage
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
@login_required
def Index(request, key_of=0):
    product = Product.objects.all().order_by('pk')
    cart, alert, total = {}, '', 0
    storage_order_object = []

    
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
        if amount > 0:
            order = Order(total_price=item.price)
            order.save()

            order_product = Order_Product.objects.create(order_id=order, product_id=item, amount=amount)
            order_product.save()

        
        
        listed_order = []
        same_order = Order_Product.objects.filter(product_id__name__icontains=item.name)
        check_same_order = ''

        if len(same_order) > 1:
            first_order = same_order[0]
            first_order.product_id.price += same_order[1].product_id.price * same_order[1].amount
            first_order.amount += same_order[1].amount
            same_order[1].delete()
            first_order.save()
            
        order_all = Order_Product.objects.all().order_by('amount')
        
        for orders in order_all:
            listed_order.append([
                orders.product_id.name,
                orders.product_id.type_of,
                orders.product_id.price * orders.amount,
                orders.amount
            ])

            
        cart = {
            'amount': amount,
            'not_send': not_send,
            'list_of_orders': listed_order,
            'number_page': key_of
        }
        #Sum Price Order All
        price_all = 0
        
        
        if len(Order.objects.filter(total_all__gt=0)) == 0:
            for price_of_order in Order_Product.objects.all():
                price_all += (price_of_order.product_id.price * price_of_order.amount)
            temp = Order.objects.create(total_price=price_all, total_all=price_all)
            temp.save()
            total = price_all
            
            
        elif len(Order.objects.filter(total_all__gt=0)) != 0:
            for price_of_order in Order_Product.objects.all():
                price_all += (price_of_order.product_id.price * price_of_order.amount)
            total_order = Order.objects.filter(total_all__gt=0)[0]
            total_order.total_all = price_all
            total_order.save()
            total = total_order.total_all
            
            
    
        
    #Show Product in Cart
    if request.method == 'GET' and Order_Product.objects.all() != None:
        
        if len(Order.objects.filter(total_all__gt=0)) != 0:
            total = Order.objects.filter(total_all__gt=0)[0].total_all

        show = Order_Product.objects.all().order_by('amount')
        listed_show = []
        for orders in show:
            listed_show.append([
                orders.product_id.name,
                orders.product_id.type_of,
                orders.product_id.price * orders.amount,
                orders.amount
            ])

            
        cart = {
            'amount': 10,
            'not_send': '',
            'list_of_orders': listed_show,
            'number_page': key_of,
            'price_total': total
        }
        

    
    return render(request, 'index/index.html', context = {
        'product': product,
        'alert': alert,
        'name': request.user.username,
        'cart': cart,
        'number_counter': key_of,
        'price_total': total
    })

    
#Delete Order
def Delete(request, number_of_page):
    
    if request.method == 'POST':
        subtract = Order.objects.filter(total_all__gt=0)[0]
        find_value = request.POST.get('delete')
        
        find_objects = Order_Product.objects.filter(product_id__name__icontains = find_value)
        
        for items in find_objects:
            subtract.total_all -= (items.product_id.price * items.amount)
        subtract.save()

        find_objects.delete()
        
    return redirect('/index/')


# Save Order and Product
def Save(request):
    
    if request.method == 'POST':
        save_order = Order_Product.objects.all()
        price_all = Order.objects.filter(total_all__gt=0)[0].total_all
        
        for items in save_order:
            product = items.product_id
            order = items.order_id
            
            s = Order_Product_Storage.objects.create(storage_order=order, storage_product=product, storage_price_all=product.price * items.amount , storage_amount_all=items.amount)
            s.save()
        
        price_all = Order.objects.filter(total_all__gt=0)
        price_all.delete()
        save_order.delete()

    return redirect('/index/')