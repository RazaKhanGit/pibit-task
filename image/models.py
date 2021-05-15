from django.db import models

# Create your models here.

class ImageM(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    info = models.TextField()
    
    def __str__(self):
        return self.title
