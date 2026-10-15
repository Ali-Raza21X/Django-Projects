from django.db import models

# Create your models here.

# class person_details(models.Model):
#     first_name=models.CharField(max_length=255)
#     last_name=models.CharField(max_length=255)


class Task(models.Model):
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    status=models.BooleanField(default=True)
