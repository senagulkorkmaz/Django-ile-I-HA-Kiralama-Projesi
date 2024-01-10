from django.db import models

class IHA(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    agirlik = models.FloatField()
    kategori = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.marka} - {self.model}"


class Kiralama(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    tarih = models.DateField()
    saat_araligi = models.CharField(max_length=100)
    kiralayan_uye = models.ForeignKey('auth.User', on_delete=models.CASCADE)
