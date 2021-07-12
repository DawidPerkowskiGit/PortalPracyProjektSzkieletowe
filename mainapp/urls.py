from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dodajogloszenie/', views.dodajogloszenie, name = 'dodajogloszenie'),
    path('przegladaj/', views.przegladaj, name = 'przegladaj'),
    path('pracodawcy/', views.pracodawcy, name = 'pracodawcy'),
    path('szczegoly_ogloszenia/<int:pk>' , views.szczegoly_ogloszenia , name = 'szczegoly_ogloszenia'),
    path('przegladaj/dodaj/', views.dodaj_ogloszenie, name = 'dodaj_ogloszenie'),
    path('szczegoly_ogloszenia/<int:pk>/odpowiedzi' , views.odpowiedz_ogloszenie , name = 'odpowiedz_ogloszenie'),
]