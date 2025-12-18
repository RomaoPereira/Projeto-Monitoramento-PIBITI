from django.urls import path
from . import views

urlpatterns = [
    path('/', views.lista_relatorio, name='lista_relatorio'),
    path('relatorios/novo/', views.cadastro_relatorio, name='cadastro_relatorio'),
    path('relatorios/editar/<int:id>/', views.editar_relatorio, name='editar_relatorio'),
]