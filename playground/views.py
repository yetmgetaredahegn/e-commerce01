from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product, OrderItem



def say_hello(request):
   #select_related(1) 1-1 1-n
   # prefetch_related(n) n-n
   queryset = Product.objects.prefetch_related("promotions").select_related('collection').all()
    
   
   return render(request, 'hello.html', {'name': 'Mosh', 'products': list(queryset)})
