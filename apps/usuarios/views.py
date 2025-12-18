from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Usuario
from .forms import UserForm, UsuarioExtraForm

def lista_usuario(request):
    usuarios = Usuario.objects.select_related('user').all()
    return render(request, 'usuarios/lista.html', {'Usuarios': usuarios})

def cadastro_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        extra_form = UsuarioExtraForm(request.POST)
        if user_form.is_valid() and extra_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            usuario = extra_form.save(commit=False)
            usuario.user = user
            usuario.save()
            return redirect('lista_usuario')
    else:
        user_form = UserForm()
        extra_form = UsuarioExtraForm()
    return render(request, 'usuarios/form.html', {'user_form': user_form, 'extra_form': extra_form, 'titulo': 'Novo Usuário'})

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=usuario.user)
        extra_form = UsuarioExtraForm(request.POST, instance=usuario)
        if user_form.is_valid() and extra_form.is_valid():
            user_form.save()
            extra_form.save()
            return redirect('lista_usuario')
    else:
        user_form = UserForm(instance=usuario.user)
        extra_form = UsuarioExtraForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'user_form': user_form, 'extra_form': extra_form, 'titulo': 'Editar Usuário'})