from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order



def say_hello(request):
   result = Order.objects.filter(customer_id=1).aggregate(count_orders= Count('id'))
    
   
   return render(request, 'hello.html', {'name': 'Yetmgeta', 'result': result})
