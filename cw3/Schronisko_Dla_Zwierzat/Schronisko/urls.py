from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('pracownicy/', views.PracownikLista, name='pracownik'),
    path('pracownicy/<int:pk>', views.PracownikSzczegoly.as_view()),
]
