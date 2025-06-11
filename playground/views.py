from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product



def say_hello(request):
   queryset = Product.objects.filter(inventory=F('collection'))
    
   
   return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
