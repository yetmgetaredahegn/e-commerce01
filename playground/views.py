from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order



def say_hello(request):
   result = OrderItem.objects.filter(product_id=1).aggregate(unit_sold= Sum('quantity'))
    
   
   return render(request, 'hello.html', {'name': 'Yetmgeta', 'result': result})
