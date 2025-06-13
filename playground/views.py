from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection,OrderItem,Order,Customer
from tags.models import TaggedItem

def say_hello(request):
   collection = Collection()
   collection.title=  "Videp Games"
   collection.featured_product = Product(pk=1)
   collection.save()

   Collection.objects.create(title='PC',featured_product_id=2)
    
   return render(request, 'hello.html', {'name': 'Yetmgeta'})
