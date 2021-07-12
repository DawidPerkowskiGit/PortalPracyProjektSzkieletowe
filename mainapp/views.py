from django.shortcuts import render, get_object_or_404
from mainapp.models import Ogloszenie
from mainapp.models import Przedsiebiorstwo
from mainapp.models import Wymaganie
from mainapp.models import Uzytkownik
from mainapp.models import OdpowiedzNaOgloszenie
from mainapp.models import OdpowiedzNaWymaganie
from .forms import OgloszenieFormularz
from .forms import OgloszenieOdpowiedz
from django.shortcuts import redirect







def home(request):
    return render(request, 'home.html')

def dodajogloszenie(request):
    return render(request, 'dodajogloszenie.html')

def przegladaj(request):
    listaOgloszen = Ogloszenie.objects.all()
    listaWymagan = Wymaganie.objects.all()
    danePracodawcy = Przedsiebiorstwo.objects.all()
    return render(request, 'przegladaj.html' , {
        'listaOgloszen' : listaOgloszen,
        'listaWymagan' : listaWymagan,
        'danePracodawcy' : danePracodawcy
        }
    )

def pracodawcy(request):
    listaPrzedsiebiorstw = Przedsiebiorstwo.objects.all()
    return render(request, 'pracodawcy.html' , {'listaPrzedsiebiorstw' : listaPrzedsiebiorstw})

def szczegoly_ogloszenia(request, pk):
    listaOgloszen = Ogloszenie.objects.all()
    listaWymagan = Wymaganie.objects.all()
    danePracodawcy = Przedsiebiorstwo.objects.all()
    listaOdpowiedzi = OdpowiedzNaOgloszenie.objects.all()
    szczegoly_ogloszenia = get_object_or_404(Ogloszenie, pk=pk)
    return render(request, 'szczegoly_ogloszenia.html' , {
        'listaOgloszen' : listaOgloszen,
        'listaWymagan' : listaWymagan,
        'danePracodawcy' : danePracodawcy,
        'listaOdpowiedzi' : listaOdpowiedzi,
        'szczegoly_ogloszenia' : szczegoly_ogloszenia
        }
    )


def dodaj_ogloszenie(request):
    if request.method == "POST":
        dodaj_ogloszenie = OgloszenieFormularz(request.POST)
        if dodaj_ogloszenie.is_valid():
            ogloszenie = dodaj_ogloszenie.save(commit=False)
            ogloszenie.save()
            return redirect('szczegoly_ogloszenia', pk=ogloszenie.pk)
    else:
        dodaj_ogloszenie = OgloszenieFormularz()
    return render(request, 'dodaj_ogloszenie.html', {'dodaj_ogloszenie': dodaj_ogloszenie})

def odpowiedz_ogloszenie(request, pk):
    if request.method == "POST":
        odpowiedz_ogloszenie = OgloszenieOdpowiedz(request.POST)
        if odpowiedz_ogloszenie.is_valid():
            odpowiedz = odpowiedz_ogloszenie.save(commit=False)
            odpowiedz.save()
            return redirect('szczegoly_ogloszenia', pk=odpowiedz.pk)
    else:
        odpowiedz_ogloszenie = OgloszenieOdpowiedz()
    return render(request, 'odpowiedz_ogloszenie.html', {'odpowiedz_ogloszenie': odpowiedz_ogloszenie})

