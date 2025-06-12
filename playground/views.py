from django.shortcuts import render
from django.db.models import Value,F,Func, Count
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer



def say_hello(request):
   queryset = Customer.objects.annotate(
      full_name=Func(F('first_name'), Value(' '), F('last_name'),function='CONCAT')
   )
   queryset = Customer.objects.annotate(
      orders_count=Count('order')
   )
    
   
   return render(request, 'hello.html', {'name': 'Yetmgeta', 'result': list(queryset)})
