from django.shortcuts import render, redirect

from Management.models import Product, Type




def manage(request):
    type_value, food, price = '', '', ''
    type_all = Type.objects.all()
    
    if request.method == 'POST':
        type_value = request.POST.get('type')
        food = request.POST.get('add')
        price = '{:.2f}'.format(float(request.POST.get('price')))
    
    return render(request, 'Management/Management.html', context = {
        'name': request.user.username,
        'type_all': type_all,
        'value': type_value,
        'food': food,
        'price': price
    })
    


