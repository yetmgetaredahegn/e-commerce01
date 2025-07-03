from codecs import lookup
import pprint
from django.db import router
from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products',views.ProductViewSet, basename='products')
router.register('collections',views.CollectionViewSet)
router.register('carts',views.CartViewSet)
router.register('customers',views.CustomerViewSet)

products_router = routers.NestedDefaultRouter(router,'products', lookup='product')
products_router.register('reviews',views.ReviewViewSet,basename='product-reviews')
items_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
items_router.register('items',views.CartItemViewSet,basename='cart-items')


urlpatterns= router.urls + products_router.urls + items_router.urls
