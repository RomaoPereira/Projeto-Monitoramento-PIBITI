from django.urls import path
from . import views

urlpatterns = [
    path('/', views.lista_usuario, name='lista_usuario'),
    path('usuarios/novo/', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
]