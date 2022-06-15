from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
router.register('category', views.CategoryViewSet)
router.register('order', views.OrderViewSet)
router.register('cart', views.CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
