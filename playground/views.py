from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product, OrderItem, Order



def say_hello(request):
   #select_related(1) 1-1 1-n
   # prefetch_related(n) n-n
   # queryset = Product.objects.prefetch_related("promotions").select_related('collection').all()
   queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
   
    
   
   return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
