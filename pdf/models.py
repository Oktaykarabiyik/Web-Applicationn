from django.db import models

# Create your models here.
class Pdf(models.Model):
    kullanici_adi=models.CharField(max_length=100)
    pdf=models.FileField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kullanici_adi    