from rest_framework import serializers
from .models import Product

# Product model serializer for showing list of all products using API
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id', 
            'title',
            'category',
            'slug',
            'product_image',
            'colors',
            'product_features',
            'star_rating',
            'percent_rating',
            'price',
            'discount',
            'discounted_price',
            'description',
            'stock_status',
            'publish',
        )
        model = Product
