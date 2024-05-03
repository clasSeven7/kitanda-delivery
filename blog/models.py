from django.db import models


class Blog(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/images/', null=True, blank=True)

    def __str__(self):
        return self.title