from rest_framework import serializers
from .models import *


class ZwierzeSerializer(serializers.Serializer):
    id = serializers
    gatunek = serializers.CharField(max_length=4, choices=Zwierze.GATUNEK_CHOICES)
    imie = serializers.CharField(max_length=45)
