from django.contrib import admin
from .models import Product, Brand, Category



# Product model admin register and settings
admin.site.register(Product)


# Brand model admin register and settings
admin.site.register(Brand)


# Category model admin register and settings
admin.site.register(Category)