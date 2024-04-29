from django.db import models

# Create your models here.

class Blog(models.Model):
    user = models.TextField()
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    # image = models.ImageField(upload_to='blogs/images/')
    
    def __str__(self):
        return self.title