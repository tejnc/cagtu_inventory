from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework import permissions
from products.models import Products


class ListProduct(generics.ListCreateAPIView):    
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Products.objects.all()
    serializer_class = ProductSerializer