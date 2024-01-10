from django.urls import path
from . import views

urlpatterns = [
    path('anasayfa/', views.anasayfa, name='anasayfa'),
    path('iha_ekle/', views.iha_ekle_view, name='iha_ekle'),
    path('iha_detay/<int:pk>/', views.iha_detay_view, name='iha_detay'),
    path('iha_sil/<int:pk>/', views.iha_sil_view, name='iha_sil'),
    path('iha/<int:pk>/duzenle/', views.iha_duzenle_view, name='iha_duzenle'),

    path('kiralama_ekle/', views.kiralama_ekle_view, name='kiralama_ekle'),
    path('kiralama/<int:kiralama_id>/sil/', views.kiralama_sil, name='kiralama_sil'),
    path('kiralama/<int:kiralama_id>/guncelle/', views.kiralama_guncelle, name='kiralama_guncelle'),
    path('kiralama/<int:kiralama_id>/', views.kiralama_detay, name='kiralama_detay'),

]
