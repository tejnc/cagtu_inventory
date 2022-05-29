from rest_framework import serializers
from products.models import Products


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        field = (
            'id',
            'Name',
            'Description',
            'Price'
        )
        model = Products
