from django.urls import path
from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.ProductsList.as_view(), name='products_list')  # list of all products API url
]