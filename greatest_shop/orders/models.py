from django.db import models
from django.contrib.auth.models import User



STATUS_CHOICES = (
    ('NEW', 'New'),
    ('IN_PROGRESS', 'In progress'),
    ('DONE', 'Done'),
)



class Order(models.Model):
    items = models.ManyToManyField('products.Item', related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='NEW')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ: {self.id}'
