from django.shortcuts import render, redirect, get_object_or_404
from .form import salaForm
from .models import Sala

# Create your views here.

def lista_sala(request):
    salas = Sala.objects.all()

    context = {'Salas': salas}

    return render(request, 'sala/lista.html', context)

def cadastro_sala(request):
    if request.method == 'POST':
        form = salaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_sala')
    else:
        form = salaForm()

    return render(request, 'sala/cadastro.html', {'form': form})

def editar_sala(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == 'POST':
        form = salaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('lista_sala')
    else:
        form = salaForm(instance=sala)
    return render(request, 'sala/cadastro.html', {'form': form})
