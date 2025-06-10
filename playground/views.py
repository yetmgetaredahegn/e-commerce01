from django.shortcuts import render
# from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product



def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    queryset = Product.objects.filter(pk=0).first()  #better way

   
    return render(request, 'hello.html', {'name': 'Mosh'})
