from django.contrib import admin
from .models import Product, Category



# Product model admin register and settings
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # change title in admin panel filter section.  'By defult_title' ---> 'By YOUR_TITLE'
    def custom_titled_filter(title):
        class Wrapper(admin.FieldListFilter):
            def __new__(cls, *args, **kwargs):
                instance = admin.FieldListFilter.create(*args, **kwargs)
                instance.title = title
                return instance
        return Wrapper

    list_display = (
        'name',
        'show_product_image',    #‌ method in models.py
        'brand',
        'category',
        'star_rating',  
        'percent_rating',
        'price',
        'discount',
        'discounted_price',
        'stock_status',
        'publish',
        'publish_status'
    )
    list_filter = (
        'brand__username',
        ('category__name', custom_titled_filter('category name')),      #‌ 'by category name' instead 'by name' (it's better to underestand).
        'stock_status',
        'publish_status',
        'publish'
    )
    search_fields = (
        'name',
        'description'
    )



# Category model admin register and settings
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'publish', 
        'publish_status'
    )
    list_filter = (
        'publish',
        'publish_status'
    )
    search_fields = (
        'name',
    )