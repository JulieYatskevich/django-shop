from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    items = models.ManyToManyField('products.Product', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Cart for {self.user}'
