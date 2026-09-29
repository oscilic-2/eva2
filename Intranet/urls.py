from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('<str:modelo>/', views.lista_modelo, name='lista_modelo'),
]