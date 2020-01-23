from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('pracownicy/', views.PracownikLista.as_view(), name='pracownik'),
    path('pracownicy/<int:pk>', views.PracownikSzczegoly.as_view()),
    path('typ_umowy/', views.TypUmowyLista.as_view(), name='typ_umowy'),
]
