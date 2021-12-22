from django.db import models
from django.utils import timezone


# abstract base model
class BaseModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish_status = models.BooleanField(default=True)                                # object publish allow

    def __str__(self):
        return self.name            # return title of product in admin pannel

    class Meta:
        abstract = True
        ordering = ['-publish']     # ascending arrangement



# model for brand of a product
class Brand(BaseModel):
    pass



# model for category of a product
class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'categories'    # categories instead categorys(typo) in model



# model for products
class Product(BaseModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_image = models.ImageField(max_length=250, blank=True, null=True, upload_to='images')
    colors = models.CharField(max_length=100)
    product_features = models.TextField()
    star_rating = models.CharField(max_length=10)                                     # rate based on stars like 4.4
    percent_rating = models.CharField(max_length=10)                                  # rate based on percent like %10
    price = models.IntegerField()
    discount = models.CharField(max_length=10, blank=True, null=True)
    discounted_price = models.IntegerField(blank=True, null=True)                     # product price after calculating the discount
    description = models.TextField()
    stock_status = models.CharField(max_length=50, blank=True, null=True)             # condition of the product in the stock