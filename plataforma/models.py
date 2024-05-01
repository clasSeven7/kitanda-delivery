from django.db import models

# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='resources/images/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/images/', null=True, blank=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    stars = models.FloatField()
    image = models.ImageField(upload_to='comments/images/', )
    
    def __str__(self):
        return self.title



