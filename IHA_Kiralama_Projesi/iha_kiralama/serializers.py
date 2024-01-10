from rest_framework import serializers
from .models import IHA, Kiralama
from django import forms


class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = ['marka', 'model', 'agirlik', 'kategori']


class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = ['iha', 'tarih', 'saat_araligi', 'kiralayan_uye']
