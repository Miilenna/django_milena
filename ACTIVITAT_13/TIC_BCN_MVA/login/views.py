from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Mostra el formulari de login si no hi ha sessió activa
def login_form(request):
    if 'usuario_id' in request.session:
        return redirect('inici')  # Si ja està autenticat, va a la pàgina d'inici
    return render(request, 'login.html')

# Processa el login i guarda la ID de l’usuari a la sessió
def process_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasenya = request.POST.get('contrasenya')

        try:
            user = User.objects.get(email=email)

            if user.check_password(contrasenya):
                request.session['usuario_id'] = user.id
                request.session['usuario_nombre'] = user.username  # Per mostrar el nom després
                return redirect('inici')
            else:
                return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

    return redirect('login_form')

# Mostra la pàgina d'inici només si l'usuari està autenticat
def inici(request):
    usuario_id = request.session.get('usuario_id')

    if usuario_id:
        usuario_nombre = request.session.get('usuario_nombre', 'Usuari')
        return render(request, 'inici.html', {'usuario': usuario_nombre})
    else:
        return redirect('login_form')

# Tanca la sessió i esborra les dades
def logout(request):
    request.session.flush()  # Elimina totes les dades de la sessió
    return redirect('login_form')