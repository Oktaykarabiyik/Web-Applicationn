from django.db import models

# Create your models here.
class Post(models.Model):
    başlık=models.CharField(max_length=120)
    metin=models.TextField()
    yayınlama_tarihi=models.DateTimeField