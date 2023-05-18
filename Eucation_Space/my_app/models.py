from django.db import models
from django.contrib.auth.models import User
import rest_framework

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta1:
         ordering = ('name',)
         verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', blank=True, null=True, on_delete=models.CASCADE)
    title_name = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='imageыs/', blank=True, null=False)
    price = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.title_name

    