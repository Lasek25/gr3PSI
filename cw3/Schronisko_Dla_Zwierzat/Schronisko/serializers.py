from rest_framework import serializers
from .models import *


class ZwierzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zwierze
        fields = ['id', 'gatunek', 'imie', 'rasa', 'plec', 'data_przyjecia',
                  'pracownik', 'boks']
    # id = serializers
    # gatunek = serializers.CharField(max_length=4, choices=Zwierze.GATUNEK_CHOICES)
    # imie = serializers.CharField(max_length=45)


class BoksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boks
        fields = ['id', 'strefa', 'pracownik']
        # fields = '__all__'


class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = ['id', 'imie', 'nazwisko', 'pesel', 'telefon', 'umowa']


class UmowaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umowa
        fields = ['id', 'data_zatrudnienia', 'data_konca_umowy', 'nr_konta', 'typ_umowy']


class TypUmowySerializer(serializers.ModelSerializer):
    class Meta:
        model = Typ_Umowy
        fields = ['id', 'stanowisko', 'pensja']