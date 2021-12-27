from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from products.models import Product

import urllib.request
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image



class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # download image from product_image_url and save it in product_image for saving in the database.
    def download_image(self, request, product_name):
        try:     # if user send an url.
            product_image_url = request.data['product_image']
            result = urllib.request.urlretrieve(product_image_url)[0]
            img_pil = Image.open(result)
            io = BytesIO()
            img_pil.save(io, format="JPEG")
            image_file = InMemoryUploadedFile(io, "product_image", product_name+'.jpg', 'image/jpeg', img_pil.size, None)   # (io, field, name, postfix, size, charest)
            image_file.seek(0)
            request.data["product_image"] = image_file
        except:    # if user send an image file.
            pass
        
        return request


    def list(self, request):
        products = self.queryset.filter(brand=request.user)       #‌ every user(vendor) just can see own products.
        serializer = self.serializer_class(products, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset.filter(brand=request.user), pk=pk)
        serializer = self.serializer_class(product, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        request = self.download_image(request, request.data['name'])

        serializer = self.serializer_class(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        # check user edit product_image or not, and then check that it is url or not.
        if request.data['product_image']:
            request = self.download_image(request, product.name)
        serializer = self.serializer_class(product, data=request.data, partial=True, context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        get_object_or_404(self.queryset, pk=pk).delete()
        return Response(status=status.HTTP_200_OK)  