from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework import status
from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Hello world!!! Congratulation if you see this text, everything is ok")


class PracownikLista(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        pracownicy = Pracownik.objects.all()
        serializer = PracownikSerializer(pracownicy, many=True)
        return Response(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = PracownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)