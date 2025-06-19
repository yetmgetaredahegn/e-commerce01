from dataclasses import field, fields
from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']
  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','slug','inventory','unit_price','paying_tax','collection']

    paying_tax = serializers.SerializerMethodField(method_name='calculate_tax')
  
    
    def calculate_tax(self,product: Product):
        return product.unit_price * Decimal(1.1)