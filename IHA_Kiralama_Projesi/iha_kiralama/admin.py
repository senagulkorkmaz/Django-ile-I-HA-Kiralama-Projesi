from django.contrib import admin
from iha_kiralama.models import IHA,Kiralama

@admin.register(IHA)
class IHAAdmin(admin.ModelAdmin):
    list_display = ['marka','model','agirlik','kategori']


@admin.register(Kiralama)
class KiralamaAdmin(admin.ModelAdmin):
    list_display = ['iha','tarih','saat_araligi','kiralayan_uye']