from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_sala, name='lista_sala'),
    path('novo/', views.cadastro_sala, name='cadastro_sala'),
    path('editar/<int:id>/', views.editar_sala, name='editar_sala'),
]
