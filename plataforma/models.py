from django.db import models

# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    # image = models.ImageField(upload_to='resources/images/')
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.URLField()
    stars = models.FloatField()
    # image = models.ImageField(upload_to='products/images/')
    
    def __str__(self):
        return self.title

class Categorie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    # image = models.ImageField(upload_to='categories/images/')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    stars = models.FloatField()
    # image = models.ImageField(upload_to='comments/images/')
    
    def __str__(self):
        return self.title


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email
    
class Register(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

