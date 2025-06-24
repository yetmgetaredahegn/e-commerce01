from itertools import product
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from store.filters import ProductFilter
from store.pagination import DefaultPagination
from .models import Cart, CartItem, Collection, OrderItem, Product, Review
from .serializers import CartSerializer, CollectionSerializer, ProductSerializer, ReviewSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price','last_update']
    
    def get_serializer_context(self):
        return {'request': self.request}
    


    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        collection_id = kwargs['pk']
        if Product.objects.filter(collection_id=collection_id).exists():
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)



    
class CartViewSet(CreateModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     # cartitem = CartItem.objects.filter(cart_id=kwargs['pk']).all()
    #     cart = self.get_object()
    #     serializer = self.get_serializer(cart)

    #     items = cart.items.all()
    #     items_serializer = self.get_serializer(items, many=True)
    #     # product = items.product.all()

    #     # data = serializer.data
    #     # data['items'] = items_serializer.data
    #     data = items_serializer.data
        

    #     return Response(data)

    


