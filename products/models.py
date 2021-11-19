from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    STATUS_CHOICES = (
        ('p', 'Published'),
        ('c', 'Checking')
    )

    name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    product_image = models.ImageField(upload_to='iamges')
    price = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   
