from django import forms

from .models import Ogloszenie
from .models import OdpowiedzNaOgloszenie


class OgloszenieFormularz(forms.ModelForm):

    class Meta:
        model = Ogloszenie
        fields = ('przedsiebiorstwo' , 'nazwa' , 'stanowisko' , 'staz' , 'branza' , 'zawod' , 'do_kiedy_aktualna' , 'praca_zdalna')

class OgloszenieOdpowiedz(forms.ModelForm):

    class Meta:
        model = OdpowiedzNaOgloszenie
        fields = ('uzytkownik' , 'ogloszenie' , 'tytul')