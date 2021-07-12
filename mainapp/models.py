from django.db import models

class Przedsiebiorstwo(models.Model):
    verbose_name_plural = "Przedsiebiorstwa"
    nazwa = models.CharField(max_length = 100)
    adres = models.CharField(max_length = 100)
    opis = models.CharField(max_length = 100)

    def returnNazwaPrzedsiebiorstwa(self):
        return self.nazwa

    def __str__(self):
        return self.nazwa

class Ogloszenie(models.Model):
    verbose_name_plural = "Ogloszenia"
    przedsiebiorstwo = models.ForeignKey(Przedsiebiorstwo, on_delete = models.CASCADE)
    nazwa = models.CharField(max_length = 30)
    stanowisko = models.CharField(max_length = 30)
    staz = models.CharField(max_length = 30)
    branza = models.CharField(max_length = 30)
    zawod = models.CharField(max_length = 30)
    do_kiedy_aktualna = models.DateField()
    praca_zdalna = models.BooleanField()

    def __str__(self):
        return self.nazwa

class Wymaganie(models.Model):
    verbose_name_plural = "Wymagania"
    ogloszenie = models.ForeignKey(Ogloszenie, on_delete = models.CASCADE)
    nazwa = models.CharField(max_length = 30)
    opis_wymagania = models.CharField(max_length = 500)

    def __str__(self):
        return self.nazwa

class Uzytkownik(models.Model):
    verbose_name_plural = "Uzytkownicy"
    login = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 30)
    imie = models.CharField(max_length = 30)
    nazwisko = models.CharField(max_length = 30)
    adres = models.CharField(max_length = 30)
    #rodzaj_wyksztalcenia = models.CharField(max_length = 30)
    #staz = models.CharField(max_length = 30)

    def __str__(self):
        return self.imie


class OdpowiedzNaOgloszenie(models.Model):
    verbose_name_plural = "Odpowiedzi na ogloszenie"
    uzytkownik = models.ForeignKey(Uzytkownik, on_delete = models.CASCADE, null = True)
    ogloszenie = models.ForeignKey(Ogloszenie, on_delete = models.CASCADE)
    tytul = models.CharField(max_length = 50, default = "Opowiedz na ogloszenie")

    def __str__(self):
        return self.tytul


class OdpowiedzNaWymaganie(models.Model):
    verbose_name_plural = "Odpowiedzi na wymaganie"
    wymaganie = models.ForeignKey(Wymaganie, on_delete = models.CASCADE)
    odpowiedz_opisowa = models.CharField(max_length = 500)

    def __str__(self):
        return self.wymaganie



