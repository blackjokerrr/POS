from django.shortcuts import render, redirect

from django.http import HttpResponse

from Sale.models import Order_Product, Order_Product_Storage
from Management.models import Product, Order

# Create your views here.

def report(request):
    
    name_all = Product.objects.all()
    product_out = Order_Product_Storage.objects.all()
    listed_value, check_same_name = [], ''
    check_listed, total = [], 0
    dict_of_sum = {}
    temp = []
    
    for value_of_sum in product_out:
        if value_of_sum.storage_product.name not in check_listed:
            check_listed.append(value_of_sum.storage_product.name)
            dict_of_sum[value_of_sum.storage_product.name] = value_of_sum.storage_amount_all
        else:
            dict_of_sum[value_of_sum.storage_product.name] += value_of_sum.storage_amount_all
    
    
    for dict_items in check_listed:
        temp.append(dict_of_sum[dict_items])

    

    
    return render(request, 'Report/report.html', context={
        'name': request.user.username,
        'product_sum_all': dict_of_sum,
        'product_name': check_listed,
        'total_item': temp
    })