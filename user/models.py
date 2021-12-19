from django.db import models

class Pdf_kayit(models.Model):
    kullanici_adi=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='pdfs/')
    
    def __str__(self):
        return self.kullanici_adi
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.
        