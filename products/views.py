from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductsList(APIView):
    def get(self, request):
        query = Product.objects.all()
        serializers = ProductSerializer(query, many=True, context={'request':request})
        return Response(serializers.data, status=status.HTTP_200_OK)

