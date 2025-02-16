from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User


def login_form(request):
    if request.user.is_authenticated or request.session.get('usuario_id'):
        return redirect('inici')
    return render(request, 'login.html')

def login_sense_sessio(request):
        return redirect('inici')

def inici(request):
    usuario_nombre = 'Invitat'

    return render(request, 'inici.html', {'usuario': usuario_nombre})

def logout_view(request):
    request.session.flush()
    auth_logout(request)
    return redirect('login_form')
