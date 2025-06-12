from django.shortcuts import render
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, OrderItem, Order



def say_hello(request):
   result = Product.objects.filter(collection_id=3).aggregate(avg_price= Avg('unit_price'), min_price=Min('unit_price'), max_price=Max('unit_price'))
    
   
   return render(request, 'hello.html', {'name': 'Yetmgeta', 'result': result})
