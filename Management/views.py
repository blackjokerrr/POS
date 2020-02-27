from django.shortcuts import render, redirect

from Management.models import Product, Type




def manage(request):
    type_value, food, price = '', '', ''
    t = Type.objects.all()
    
    if request.method == 'POST' and type_value != 'type':
        type_value = request.POST.get('type')
        food = request.POST.get('add')
        price = '{:.2f}'.format(float(request.POST.get('price')))
    
    return render(request, 'Management/Management.html', context = {'name': request.user.username,
                                                                    'type': t,
                                                                    'value': type_value,
                                                                    'food': food,
                                                                    'price': price})

