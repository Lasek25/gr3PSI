from django.db import models

class Typ_Umowy(models.Model):
    stanowisko_enum = ('opiekun', 'weterynarz', 'administracja', 'prezes')

    stanowisko = models.CharField(max_length=13, choices=stanowisko_enum)
    pensja = models.IntegerField()

class Umowa(models.Model):
    data_zatrudnienia = models.DateField()
    data_konca_umowy = models.DateField()
    nr_konta = models.CharField(max_length=26)
    typ_umowy = models.ForeignKey(Typ_Umowy, on_delete=models.SET(0))

#class Pracownik(models.Model):


class Boks(models.Model):
    strefa_enum = ('do_adopcji', 'resocjalizacja', 'młode')
    
    strefa = models.CharField(max_length=15, choices=strefa_enum)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE())

class Zwierzę(models.Model):
    gatunek_enum = ('pies', 'kot')
    plec_enum = ('samiec', 'samica')

    gatunek = models.CharField(max_length=4, choices=gatunek_enum)
    imie = models.CharField(max_length=45)
    rasa = models.CharField(max_length=45, default='mieszana')
    plec = models.CharField(max_length=45, choices=plec_enum)
    data_przyjecia = models.DateField()
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE())
    boks = models.ForeignKey(Boks,)


