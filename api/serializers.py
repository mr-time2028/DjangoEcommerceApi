from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CharField
from products.models import Product, Category
from django.utils.text import slugify


# Product model serializer
class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.PrimaryKeyRelatedField(source='brand.username', read_only=True, default=serializers.CurrentUserDefault())          # instead showing 'pk' (related to ForeignKey), showing 'username' of user.
    category = serializers.CharField(source='category.name')                                 # instead showing 'pk' (related to ForeignKey), showing 'name' of category instance.

    class Meta:
        model = Product
        fields = [
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
            'publish'
        ]


    # Category model is ForeignKey field. so we need make object for that. (sometimes maybe we have object before)
    # this method created to prevent of making an object which exist before in the database.
    def make_new_object(self, model, validated_data):
        # getting category keys to make an object with them in next part.
        model_dict = validated_data.pop(f'{type(model()).__name__.lower()}')     # convert 'Category'‌(model) to 'category'(key in validated_data)
        # we have object before, so no need to make a new object.
        try:
            obj = model.objects.get(slug=slugify(model_dict['name'], allow_unicode=True))
        # we don't have any object, so need to make a new object .
        except:
            obj = model.objects.create(name=model_dict['name'])

        return obj


    def create(self, validated_data):
        # make product object to save in the database.
        return Product.objects.create(
            brand=self.context["request"].user,
            category=self.make_new_object(Category, validated_data),
            **validated_data
        )


    def update(self, instance, validated_data):
        #‌ edit category field.
        try:
            instance.category = self.make_new_object(Category, validated_data)
        # category field not edited 
        except:
            instance.category = instance.category
        
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.product_image = instance.product_image 

        instance.save()
        return instance