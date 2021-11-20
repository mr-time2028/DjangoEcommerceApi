from django.db.models import fields
from rest_framework import serializers
from .models import Product

# Product model serializer for showing list of all products using API
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = (
            'id', 
            'name',
            'product_code',
            'slug',
            'product_image',
            'price',
            'description',
            'status',
            'publish',
        )
        model = Product
