from django.shortcuts import render, redirect

from django.http import HttpResponse

from Sale.models import Order_Product, Order_Product_Storage
from Management.models import Product, Order
from django.contrib.auth.decorators import login_required

from datetime import *
# Create your views here.

@login_required
def report(request):
    
    temp_total = 0
    get_date = datetime.now()
    current = get_date.strftime('%Y-%m-%d')
    current_use = current.split('-')
    
    objects_week, month = '', ''
    start_date = ''
    total_week, total_month, total_year = 0, 0, 0
    
    try:
        get_order = Order_Product_Storage.objects.filter(storage_order__date_time__exact=current)
        start_date = Order_Product_Storage.objects.all().order_by('pk')[0].storage_order.date_time
    except:
        print('Error')
        
    week = str(start_date).split('-')
    to_week = date(int(week[0]), int(week[1]), int(week[2]) + 7)
    start_week = date(int(week[0]), int(week[1]), int(week[2]))
    

    for value_of_sum in get_order:
        temp_total += (value_of_sum.storage_product.price * value_of_sum.storage_amount_all)
        
    if date(int(current_use[0]), int(current_use[1]), int(current_use[2])) <= to_week and start_week <= date(int(current_use[0]), int(current_use[1]), int(current_use[2])):
        try:
            objects_week = Order_Product_Storage.objects.filter(storage_order__date_time__gte=start_week, storage_order__date_time__lte=to_week)
        except:
            print('Error')
        
        for items_week in objects_week:
            
            total_week += (items_week.storage_product.price * items_week.storage_amount_all)
    
    to_month = date(int(week[0]), int(week[1]) + 1, int(week[2]))
    
    if date(int(current_use[0]), int(current_use[1]), int(current_use[2])) <= to_month and start_week <= date(int(current_use[0]), int(current_use[1]), int(current_use[2])):
        try:
            month = Order_Product_Storage.objects.filter(storage_order__date_time__gte=start_week, storage_order__date_time__lte=to_month)
        except:
            print('Error')
        
        
        for items_month in month:
            
            total_month += (items_month.storage_product.price * items_month.storage_amount_all)
            
    to_year = date(int(week[0]) + 1, int(week[1]), int(week[2]))
    
    if date(int(current_use[0]), int(current_use[1]), int(current_use[2])) <= to_month and start_week <= date(int(current_use[0]), int(current_use[1]), int(current_use[2])):
        try:
            year = Order_Product_Storage.objects.filter(storage_order__date_time__gte=start_week, storage_order__date_time__lte=to_month)
        except:
            print('Error')
            
        for items_year in year:
            
            total_year += (items_year.storage_product.price * items_year.storage_amount_all)
        
    
    
    return render(request, 'Report/report.html', context={
        'name': request.user.username,
        'total_of_day': temp_total,
        'current_day': current,
        'count_order': len(get_order),
        'show_week': start_week,
        'total_week': total_week,
        'end_week': to_week,
        'result': len(objects_week),
        'total_month': total_month,
        'count_month': len(month),
        'total_year': total_year,
        'count_year': len(year)
    })