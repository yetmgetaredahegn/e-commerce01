from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth import get_user_model
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from core.models import User

# Register your models here.


# User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    search_fields = ['first_name', 'last_name', 'email']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "usable_password",
                    "password1",
                    "password2",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )

class TagInline(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields=['tag']


admin.site.unregister(Product)

@admin.register(Product)
class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

