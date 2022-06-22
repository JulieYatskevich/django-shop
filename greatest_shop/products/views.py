from django.db import transaction

from rest_framework import viewsets, response, status
from rest_framework.decorators import action


from .models import Product, Item
from .serializers import ProductSerializer, ItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
