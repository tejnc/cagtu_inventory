from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    product = Products.objects.all()
    serializer = ItemSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()
