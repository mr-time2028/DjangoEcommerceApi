from rest_framework import routers
from . import views
from django.urls import path, include

app_name = 'products'
router = routers.DefaultRouter()
router.register(r'products', views.ProductView, basename='products')   # Get and Post url router for ProductView
urlpatterns = router.urls