from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=100)
    sku=models.CharField(max_length=30,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.PositiveIntegerField(default=0)
    low_stock_threshold=models.PositiveIntegerField(default=5)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

