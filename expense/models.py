from django.db import models

# Create your models here.

class Expense(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)




