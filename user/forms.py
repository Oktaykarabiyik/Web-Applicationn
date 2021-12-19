from django import forms
from django.http import request

from .models import Pdf_kayit

class Pdf_kayitForm(forms.ModelForm):
    class Meta:
        model=Pdf_kayit
        fields=('pdf','kullanici_adi')
