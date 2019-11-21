from django.db import models

class Typ_Umowy(models.Model):
    STANOWISKO_CHOICES = (
        ('OPIEKUN', 'opiekun'),
        ('WETERYNARZ', 'weterynarz'),
        ('ADMINISTRACJA', 'administracja'),
        ('PREZES', 'prezes'),
    )
    stanowisko = models.CharField(max_length=13, choices=STANOWISKO_CHOICES)
    pensja = models.IntegerField()


class Umowa(models.Model):
    data_zatrudnienia = models.DateField()
    data_konca_umowy = models.DateField()
    nr_konta = models.CharField(max_length=26, null=False)
    typ_umowy = models.ForeignKey(Typ_Umowy, on_delete=models.SET_NULL, null=True)


class Pracownik(models.Model):
    imie = models.CharField(max_length=45, null=False)
    nazwisko = models.CharField(max_length=45, null=False)
    pesel = models.CharField(max_length=11, null=False, unique=True)
    telefon = models.CharField(max_length=9)
    umowa = models.ForeignKey(Umowa, on_delete=models.CASCADE)


class Boks(models.Model):
    STREFA_CHOICES = (
        ('DO_ADOPCJI', 'do_adopcji'),
        ('RESOCJALIZACJA', 'resocjalizacja'),
        ('MLODE', 'młode'),
    )
    strefa = models.CharField(max_length=15, choices=STREFA_CHOICES)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.SET_NULL, null=True)


class Zwierze(models.Model):
    GATUNEK_CHOICES = (
        ('PIES', 'pies'),
        ('KOT', 'kot'),
    )
    PLEC_CHOICES = (
        ('SAMIEC', 'samiec'),
        ('SAMICA', 'samica'),
    )
    gatunek = models.CharField(max_length=4, choices=GATUNEK_CHOICES)
    imie = models.CharField(max_length=45)
    rasa = models.CharField(max_length=45, default='mieszana')
    plec = models.CharField(max_length=45, choices=PLEC_CHOICES)
    data_przyjecia = models.DateField()
    pracownik = models.ForeignKey(Pracownik, on_delete=models.SET_NULL, null=True)
    boks = models.ForeignKey(Boks, on_delete=models.SET_NULL, null=True)


