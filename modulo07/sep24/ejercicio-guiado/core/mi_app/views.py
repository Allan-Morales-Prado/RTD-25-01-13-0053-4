# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import PerfilUsuario

def modificar_edad(request, username):
    usuario = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(PerfilUsuario, user=usuario)
    if request.method == 'POST':
        nueva_edad = request.POST.get('nueva_edad')
        perfil_usuario.edad = nueva_edad
        perfil_usuario.save()

    return render(request, 'mi_app/modificar_edad.html', {'usuario': usuario, 'perfil_usuario': perfil_usuario})

def mi_perfil(request, username):
    usuario = get_object_or_404(User, username=username)
    perfil_usuario = get_object_or_404(PerfilUsuario, user=usuario)
    return render(request, 'mi_app/perfil.html', {'usuario': usuario, 'perfil_usuario': perfil_usuario})