from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


# list of all products API view
class PorductViewSet(viewsets.ViewSet):

    def list_of_products(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)



