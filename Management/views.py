from django.shortcuts import render, redirect
from django.http import HttpResponse

from Management.models import Product, Type




def manage(request):
    
    product = Product.objects.all().order_by('pk')
    type_of_product = Type.objects.all()
    set_of_search = []
    
    if request.method == 'POST':
        
        if request.POST.get('search') != '' or request.POST.get('choose_type') != '0':
            search_items = request.POST.get('search')
            choose_type = request.POST.get('choose_type')
             
            set_type = Product.objects.filter(type_of__name__icontains=choose_type)
            
            set_of_name = Product.objects.filter(name__icontains=search_items)
            
            if len(set_type) != 0 and len(set_of_name) == 0:
                set_of_search = set_type
                
            elif len(set_type) == 0 and len(set_of_name) != 0:
                set_of_search = set_of_name
                
            elif len(set_type) != 0 and len(set_of_name) != 0:
                for checker in set_type:
                    if checker in set_of_name:
                        set_of_search.append(checker)
            
    
    
    return render(request, 'Management/Management.html', context={
        'name': request.user.username,
        'product': product,
        'type': type_of_product,
        'search': set_of_search
    })
    
    
def Change_product(request):
    
    if request.method == 'POST':
        find = request.POST.get('find_value')
        name = request.POST.get('change_name_of_product')
        price = request.POST.get('change_price_of_product')
        
        change_product = Product.objects.get(name__iexact=find)
        
        change_product.name = name
        change_product.price = price
        change_product.save()
        
        
    
    return redirect('/manage/')


def Change_type(request):
    
    if request.method == 'POST':
        
        find = request.POST.get('find_value')
        change_to = request.POST.get('select')
        
        product_find = Product.objects.get(name__iexact=find)
        
        get_type = Type.objects.get(name__iexact=change_to)
        
        product_find.type_of = get_type
        product_find.save()
        
        
    return redirect('/manage/')
        
        
def Delete(request):
    
    if request.method == 'POST':
        
        get_index = request.POST.get('index')
        
        find_product_to_delete = Product.objects.get(name__iexact=get_index)
        find_product_to_delete.delete()
        
        
    return redirect('/manage/')


def Add_product(request):
    
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            
            type_of_product = request.POST.get('type')
            get_type = Type.objects.get(name__iexact=type_of_product)
            
            price = request.POST.get('price')
            storage = request.POST.get('storage')

            create_product = Product.objects.create(name=name, type_of=get_type, price=price, storage=storage)
            create_product.save()
        except:
            print('Error')

        
        
    return redirect('/manage/')


def Add_type(request):
    
    if request.method == 'POST':
        
        add = request.POST.get('add_type')
        
        add_to = Type.objects.create(name=add)
        add_to.save()
        
    return redirect('/manage/')