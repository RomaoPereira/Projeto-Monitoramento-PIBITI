from django.shortcuts import render, get_object_or_404, redirect
from .models import Leitura
from .forms import LeituraForms

def lista_leitura(request):
    # Usamos select_related para carregar o nome da sala de forma rápida
    leituras = Leitura.objects.select_related('sala').all()
    return render(request, 'leitura/lista.html', {'Leituras': leituras})

def cadastro_leitura(request):
    if request.method == 'POST':
        form = LeituraForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_leitura')
    else:
        form = LeituraForms()
    return render(request, 'leitura/forms.html', {'form': form, 'titulo': 'Nova Leitura'})

def editar_leitura(request, id):
    leitura = get_object_or_404(Leitura, id=id)
    if request.method == 'POST':
        form = LeituraForms(request.POST, instance=leitura)
        if form.is_valid():
            form.save()
            return redirect('lista_leitura')
    else:
        form = LeituraForms(instance=leitura)
    return render(request, 'leitura/form.html', {'form': form, 'titulo': 'Editar Leitura'})