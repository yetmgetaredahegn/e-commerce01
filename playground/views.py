from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
   # custom managers
   queryset=TaggedItem.objects.get_tags_for(Product,1)
   
   return render(request, 'hello.html', {'name': 'Yetmgeta', 'tags': list(queryset)})
