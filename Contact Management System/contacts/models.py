from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
      regex=r"^\+?1?\d{9,15}$",
      message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
  )
# Create your models here.

class Contact(models.Model):
    fullname=models.CharField(unique=True,blank=False)
    email=models.EmailField(unique=True,)
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    address=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    

    