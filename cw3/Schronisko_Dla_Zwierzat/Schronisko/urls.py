from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
<<<<<<< HEAD:Schronisko_Dla_Zwierzat/Schronisko/urls.py
    path('pracownicy/', views.pracownik, name='pracownik'),
=======
    path('pracownicy/', views.PracownikLista, name='pracownik'),
>>>>>>> origin/master:cw3/Schronisko_Dla_Zwierzat/Schronisko/urls.py
]