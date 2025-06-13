from django.shortcuts import render
from django.db import transaction
from store.models import Product, Collection,OrderItem,Order,Customer
from tags.models import TaggedItem

# @transaction.atomic() get every in the func into trasaction
def say_hello(request):
 #... lets say there is code u don't want in the transaction
   with transaction.atomic():
      order = Order()
      order.customer_id =1
      order.save()

      item = OrderItem()
      item.order = order
      item.product_id = 1
      item.quantity = 1
      item.unit_price= 10
      item.save()

   return render(request, 'hello.html', {'name': 'Yetmgeta'})
