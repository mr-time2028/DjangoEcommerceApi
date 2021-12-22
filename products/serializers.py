from rest_framework import serializers
from .models import Product, Brand, Category
from django.utils.text import slugify


# Product model serializer
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')          # instead showing 'pk' (related to ForeignKey), showing 'name' of brand instance.
    category = serializers.CharField(source='category.name')    # instead showing 'pk' (related to ForeignKey), showing 'name' of category instance.

    class Meta:
        fields = (
            'id', 
            'name',
            'brand',
            'category',
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


    def create(self, validated_data):

        # getting brand and category keys to make an object with them in next part.
        brand_dict = validated_data.pop('brand')
        category_dict = validated_data.pop('category')

        # Brand and Category model are ForeignKey field. so we need make object for them. (sometimes maybe we have object before)
        def make_new_object(model, dict):
            try:
                obj = model.objects.get(slug=slugify(dict['name'], allow_unicode=True))
            except:
                obj = model.objects.create(name=dict['name'])
            return obj

        # make product object to save in the database.
        return Product.objects.create(brand=make_new_object(Brand, brand_dict), category=make_new_object(Category, category_dict), **validated_data)