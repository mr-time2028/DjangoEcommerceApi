from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.html import format_html


# abstract base model
class BaseModel(models.Model):
    PUBLISH_STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, allow_unicode=True)     # allow_unicode allow to put persian slug‌.    
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_status = models.CharField(max_length=15, choices=PUBLISH_STATUS_CHOICES, default='p')

    def __str__(self):
        return self.name            # return name of product

    class Meta:
        abstract = True
        ordering = ['-publish']     # desending arrangement



# model for category of a product
class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'categories'    # categories instead categorys(typo) in model



# model for products
class Product(BaseModel):
    brand = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_image = models.ImageField(upload_to='images', default='default.jpg')
    colors = models.CharField(max_length=100)
    product_features = models.TextField()
    star_rating = models.CharField(max_length=10)                                     # rate based on stars like 4.4
    percent_rating = models.CharField(max_length=10)                                  # rate based on percent like %10
    price = models.IntegerField()
    discount = models.CharField(max_length=10, blank=True, null=True)
    discounted_price = models.IntegerField(blank=True, null=True)                     # product price after calculating the discount
    description = models.TextField()
    stock_status = models.CharField(max_length=50, blank=True, null=True)             # condition of the product in the stock


    #‌ showing image instead html tags
    def show_product_image(self):
        return format_html(f"<img src='{self.product_image.url}' alt='{self.name}' width='70' height='55' style='border-radius: 3px'>")
    show_product_image.short_description = 'product image'