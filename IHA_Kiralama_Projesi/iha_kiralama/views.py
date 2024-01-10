from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import IHA, Kiralama
from .serializers import IHAForm, KiralamaForm


def anasayfa(request):
    iha_list = IHA.objects.all()
    kiralama_list = Kiralama.objects.all()
    return render(request, 'anasayfa.html', {'iha_list': iha_list, 'kiralama_list': kiralama_list})


def iha_ekle_view(request):
    if request.method == 'POST':
        # Formdan gelen verilerle bir IHAForm örneği oluşturulur
        form = IHAForm(request.POST)
        if form.is_valid():
            yeni_iha = form.save()  # Veritabanına yeni IHA kaydedilir
            # Eklendikten sonra detay sayfasına yönlendirme
            return redirect('iha_detay', pk=yeni_iha.pk)
    else:
        form = IHAForm()  # Boş bir form oluşturulur

    return render(request, 'iha_ekle.html', {'form': form})


def iha_detay_view(request, pk):
    iha = get_object_or_404(IHA, pk=pk)
    return render(request, 'iha_detay.html', {'iha': iha})


def iha_sil_view(request, pk):
    iha = get_object_or_404(IHA, pk=pk)
    if request.method == 'POST':
        iha.delete()
        # Silme işleminden sonra anasayfaya yönlendirme
        return redirect('anasayfa')
    return render(request, 'iha_sil.html', {'iha': iha})


def iha_duzenle_view(request, pk):
    iha = get_object_or_404(IHA, pk=pk)

    if request.method == 'POST':
        form = IHAForm(request.POST, instance=iha)
        if form.is_valid():
            form.save()
            return redirect(reverse('anasayfa'))
    else:
        form = IHAForm(instance=iha)

    return render(request, 'iha_duzenle.html', {'iha': iha, 'form': form})


def kiralama_ekle_view(request):
    if request.method == 'POST':
        form = KiralamaForm(request.POST)
        if form.is_valid():
            # Form verileri doğruysa
            form.save()  # Kiralama kaydını veritabanına kaydet
            # Anasayfaya yönlendirir
            return redirect('anasayfa')
    else:
        form = KiralamaForm()

    return render(request, 'kiralama_ekle.html', {'kiralama_form': form})


def kiralama_sil(request, kiralama_id):
    kiralama = get_object_or_404(Kiralama, id=kiralama_id)
    kiralama.delete()
    # Silme işlemi tamamlandıktan sonra ana sayfaya yönlendirme yapar.
    return redirect('anasayfa')


def kiralama_guncelle(request, kiralama_id):
    kiralama = get_object_or_404(Kiralama, id=kiralama_id)
    if request.method == 'POST':
        form = KiralamaForm(request.POST, instance=kiralama)
        if form.is_valid():
            form.save()
            return redirect('kiralama_detay', kiralama_id=kiralama.id)
    else:
        form = KiralamaForm(instance=kiralama)
    return render(request, 'kiralama_guncelle.html', {'form': form, 'kiralama': kiralama})


def kiralama_detay(request, kiralama_id):
    # Kiralama öğesini veritabanından al veya 404 hatası döndür
    kiralama = get_object_or_404(Kiralama, id=kiralama_id)

    return render(request, 'kiralama_detay.html', {'kiralama': kiralama})
