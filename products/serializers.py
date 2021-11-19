from django.db.models import fields
from rest_framework import serializers
from .models import Product

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
