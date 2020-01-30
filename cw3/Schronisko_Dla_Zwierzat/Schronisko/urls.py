from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('pracownicy/', views.PracownikLista.as_view(), name='pracownik'),
    path('pracownicy/<int:pk>', views.PracownikSzczegoly.as_view(), name='pracownikS'),
    path('typ_umowy/', views.TypUmowyLista.as_view(), name='typ_umowy'),
    path('typ_umowy/<int:pk>', views.TypUmowySzczegoly.as_view(), name='typ_umowy'),
    path('umowy/', views.UmowaLista.as_view(), name='umowa'),
    path('umowy/<int:pk>', views.UmowaSzczegoly.as_view(), name='boks'),
    path('boksy/', views.BoksLista.as_view(), name='umowa'),
    path('boksy/<int:pk>', views.BoksSzczegoly.as_view(), name='boksS'),
    path('zwierzeta/', views.ZwierzeLista.as_view(), name='zwierze'),
    path('zwierzeta/<int:pk>', views.ZwierzeSzczegoly.as_view(), name='zwierzeS'),
]
