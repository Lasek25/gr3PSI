from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status
from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Hello world!!! Congratulation if you see this text, everything is ok")


class PracownikLista(APIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer

    def get(self, request, format=None):
        pracownicy = Pracownik.objects.all()
        serializer = PracownikSerializer(pracownicy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PracownikSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save(owner=self.request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PracownikSzczegoly(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
# class PracownikSzczegoly(APIView):
#     permission_classes = [permissions.IsAdminUser]
#
#     def get_object(self, pk):
#         try:
#             return Pracownik.objects.get(pk=pk)
#         except Pracownik.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = PracownikSerializer(question)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         question = self.get_object(pk)
#         serializer = PracownikSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         question = self.get_object(pk)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class TypUmowyLista(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        typ_umowy = Typ_Umowy.objects.all()
        serializer = TypUmowySerializer(typ_umowy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TypUmowySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TypUmowySzczegoly(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Typ_Umowy.objects.all()
    serializer_class = TypUmowySerializer


class UmowaLista(APIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Umowa.objects.all()
    serializer_class = UmowaSerializer

    def get(self, request, format=None):
        umowy = Umowa.objects.all()
        serializer = UmowaSerializer(umowy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UmowaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UmowaSzczegoly(generics.RetrieveAPIView):
    queryset = Umowa.objects.all()
    serializer_class = UmowaSerializer


class BoksLista(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Boks.objects.all()
    serializer_class = BoksSerializer

    def get(self, request, format=None):
        boksy = Boks.objects.all()
        serializer = BoksSerializer(boksy, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BoksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoksSzczegoly(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Boks.objects.all()
    serializer_class = BoksSerializer


class ZwierzeLista(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ZwierzeSerializer

    def get_queryset(self):
        user = self.request.user
        # return Zwierze.objects.filter(autor=user)

        return Zwierze.objects.filter()

    def perform_create(self, serializer):
        user = self.request.user
        # serializer.save(autor=user)
        serializer.save()


class ZwierzeSzczegoly(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ZwierzeSerializer
    queryset = Zwierze.objects.all()


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = PracownikSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = PracownikSerializer


