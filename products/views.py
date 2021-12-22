from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

import urllib.request
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image



class ProductView(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(queryset, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        # download image from product_image_url and save it in product_image for saving in the database.
        product_image_url = request.data['product_image']
        result = urllib.request.urlretrieve(product_image_url)[0]
        img_pil = Image.open(result)
        io = BytesIO()
        img_pil.save(io, format="JPEG")
        image_file = InMemoryUploadedFile(io, 'product_image', request.data['name']+'.jpg', 'image/jpeg', img_pil.size, None)
        image_file.seek(0)
        request.data["product_image"] = image_file


        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)