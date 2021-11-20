from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from .signals import set_product_slug

# Create your models here.

# product model
class Product(models.Model):
    STATUS_CHOICES = (
        ('p', 'Published'),
        ('c', 'Checking')
    )

    name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=200, unique=True, blank=True)
    product_image = models.ImageField(upload_to='iamges', blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # return name of product in admin pannel
    def __str__(self):
        return self.name   


# signals
pre_save.connect(set_product_slug, Product)