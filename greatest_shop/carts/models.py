from django.db import models
from django.contrib.auth.models import User

from main.models import BaseModel


class Cart(BaseModel):
    items = models.ManyToManyField('products.Item', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart for {self.user}'
