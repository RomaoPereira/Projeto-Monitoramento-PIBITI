from django.shortcuts import render, get_object_or_404, redirect
from .models import Relatorio
from .forms import RelatorioForm

def lista_relatorio(request):
    # Usamos select_related para as duas FKs para otimizar o banco
    relatorios = Relatorio.objects.select_related('sala', 'usuario').all()
    return render(request, 'relatorio/lista.html', {'Relatorios': relatorios})

def cadastro_relatorio(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_relatorio')
    else:
        form = RelatorioForm()
    return render(request, 'relatorio/form.html', {'form': form, 'titulo': 'Novo Relatório'})

def editar_relatorio(request, id):
    relatorio = get_object_or_404(Relatorio, id=id)
    if request.method == 'POST':
        form = RelatorioForm(request.POST, instance=relatorio)
        if form.is_valid():
            form.save()
            return redirect('lista_relatorio')
    else:
        form = RelatorioForm(instance=relatorio)
    return render(request, 'relatorio/form.html', {'form': form, 'titulo': 'Editar Relatório'})