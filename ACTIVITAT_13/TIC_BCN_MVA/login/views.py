from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User


def login_form(request):
    if request.user.is_authenticated or request.session.get('usuario_id'):
        return redirect('inici')
    return render(request, 'login.html')


def login_sense_sessio(request):
        return redirect('inici')


def login_amb_sessio(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        contrasenya = request.POST.get('contrasenya', '')
        try:
            user = User.objects.get(email=email)
            if user.check_password(contrasenya):
                request.session['usuario_id'] = user.id
                request.session['usuario_nombre'] = user.username
                return redirect('inici')
            else:
                return render(request, 'login.html', {'error': 'Contrasenya incorrecta'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuari no existent'})
    return render(request, 'login.html')


def inici(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario_nombre = request.session.get('usuario_nombre', 'Usuari')
    else:
        usuario_nombre = 'Invitat'
    return render(request, 'inici.html', {'usuario': usuario_nombre})


def logout_view(request):
    request.session.flush()
    auth_logout(request)
    return redirect('login_form')
