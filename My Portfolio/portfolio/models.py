from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(blank=False,max_length=100)
    slug=models.SlugField(unique=True)
    short_description=models.CharField(blank=True,max_length=100)
    description=models.TextField(blank=True)
    tech_stack=models.CharField(blank=False,max_length=255)
    github_url=models.URLField(blank=True)
    live_url=models.URLField(blank=True)
    image=models.ImageField(upload_to='projects/')
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
    ("BEG", "Beginner"),
    ("INT", "Intermediate"),
    ("ADV", "Advanced"),
]
    name=models.CharField(blank=False,max_length=100)
    category=models.CharField(blank=True,max_length=100)
    proficiency=models.CharField(blank=True,max_length=100,choices=PROFICIENCY_CHOICES,default="BEG")
    display_order=models.IntegerField(default=0)

class ContactMesssage(models.Model):
    name=models.CharField(blank=False,max_length=100)
    email=models.EmailField(blank=False)
    subject=models.CharField(blank=False,max_length=100)
    message=models.TextField(blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

class Experience(models.Model):
    title=models.CharField(max_length=255,blank=False)
    organization=models.CharField(max_length=100,blank=False)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField(null=True)
    is_current=models.BooleanField(default=False)

class Education(models.Model):
    qualification=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
    description=models.TextField()
    year=models.IntegerField()

