from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product



def say_hello(request):
    #Products:inverntory < 10 and price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20) 
    # alternative
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    #Products:inverntory < 10 or price < 20
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20) )
    queryset = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20) )
    
   
    return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
