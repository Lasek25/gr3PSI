from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    pracownicy = serializers.PrimaryKeyRelatedField(many=True, queryset=Pracownik.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'pracownicy']


class ZwierzeSerializer(serializers.ModelSerializer):
    # autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = Zwierze
        fields = ['id', 'gatunek', 'imie', 'rasa', 'plec', 'data_przyjecia',
                  'pracownik', 'boks']
        # fields = ['id', 'gatunek', 'imie', 'rasa', 'plec', 'data_przyjecia',
        #           'pracownik', 'boks', 'autor']
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
        fields = ['id', 'imie', 'nazwisko', 'pesel', 'telefon']

    def create(self, validated_data):
        return Pracownik.objects.create(**validated_data)


class UmowaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umowa
        fields = ['id', 'data_zatrudnienia', 'data_konca_umowy', 'nr_konta', 'typ_umowy', 'pracownik']

    def create(self, validated_data):
        return Umowa.objects.create(**validated_data)


class TypUmowySerializer(serializers.ModelSerializer):
    class Meta:
        model = Typ_Umowy
        fields = ['id', 'stanowisko', 'pensja']

    def update(self, instance, validated_data):
        instance.pensja = validated_data.get('pensja', instance.pensja)
        instance.save()
        return instance
