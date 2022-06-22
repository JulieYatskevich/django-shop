from rest_framework import permissions
from carts.models import Cart
from rest_framework import generics
from .serializers import CartSerializer


class CartAPIList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CartAPIUpdate(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)
