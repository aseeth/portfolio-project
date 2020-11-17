from django.db import models

# Create your models here.
class Blog(models.Model):
    tittle = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')