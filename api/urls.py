from rest_framework import routers
from . import views
from django.urls import path, include


app_name = 'api'
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]