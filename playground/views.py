from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection,OrderItem,Order,Customer
from tags.models import TaggedItem

def say_hello(request):
   # collection = Collection.objects.get(pk=11) #Collection(pk=11) possible but orm of django will still update the ones thats is not mentioned like title to null
   # collection.featured_product = None
   # collection.save()

   Collection.objects.filter(pk=11).update(featured_product=None)
    
   return render(request, 'hello.html', {'name': 'Yetmgeta'})
