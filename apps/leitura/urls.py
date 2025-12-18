from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_leitura, name='lista_leitura'),
    path('leituras/novo/', views.cadastro_leitura, name='cadastro_leitura'),
    path('leituras/editar/<int:id>/', views.editar_leitura, name='editar_leitura'),
]