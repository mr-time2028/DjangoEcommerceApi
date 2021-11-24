from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from .signals import set_product_slug



# product model
class Product(models.Model):
    STATUS_CHOICES = (
        ('p', 'Published'),
        ('c', 'Checking')
    )

    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    category = models.CharField(max_length=100)
    product_image = models.URLField(max_length=250, blank=True, null=True)
    colors = models.CharField(max_length=100)
    product_features = models.TextField()
    star_rating = models.CharField(max_length=10)
    percent_rating = models.CharField(max_length=10)
    price = models.IntegerField()
    discount = models.CharField(max_length=10, blank=True, null=True)
    discounted_price = models.IntegerField(blank=True, null=True)                     # product price after calculating the discount
    description = models.TextField()
    stock_status = models.CharField(max_length=50, blank=True, null=True)             # condition of the product in the stock 
    publish_status = models.CharField(default='c', max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # return title of product in admin pannel
    def __str__(self):
        return self.title   


# signals
pre_save.connect(set_product_slug, Product)