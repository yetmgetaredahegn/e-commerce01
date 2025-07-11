from django.conf import settings
from django.contrib import admin, messages
from django.db.models import Count
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.html import format_html, urlencode
from . import models

# custom filters
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
        ]
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['clear_inventory']
    autocomplete_fields=['collection']
    list_display = ['title','unit_price', 'inventory_status','collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update',InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']
    prepopulated_fields = {
        'slug':  ['title']
    }
    search_fields=['title']

    def collection_title(self,product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return "OK"
    
    @admin.action(description='Clear inventory')
    def clear_inventory(self,request,queryset):
       updated_count = queryset.update(inventory=0)
       self.message_user(
           request,
           f'{updated_count} products were successfully updated.',
        #    messages.ERROR
       )



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['first_name','last_name', 'membership', 'orders_count']
    list_editable = ['membership']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name','user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

    @admin.display(ordering='orders_count')
    def orders_count(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({'customer': str(customer.id)})
        )
        return format_html('<a href={}>{}</a>', url,customer.orders_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )
    

class OrderItemInline(admin.TabularInline):
    autocomplete_fields=['product']
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields=['customer']
    inlines = [OrderItemInline]
    list_display = ['id','customer','payment_status']
    list_select_related = ['customer']

    @admin.display(ordering='customer')
    def customer_em(self,order):
        return order.customer.first_name
    
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields=['title']
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = (reverse('admin:store_product_changelist')
               + "?"
               + urlencode({
                   'collection__id': str(collection.id)
               })
               )
        return format_html('<a href="{}"> {} </a>',url, collection.products_count)
        
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )


