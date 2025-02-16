from django.shortcuts import render, redirect
from .forms import PersonForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

# Create your views here.
def inici(request):
    return render(request, 'inici.html')

def user_form(request):
    form = PersonForm()
    context = {'form':form}
    return render(request, 'form.html', context)


def login_form(request):
    return render(request, 'login.html')

def process_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasenya = request.POST.get('contrasenya')

        try:
            user = User.objects.get(email=email)

            if user.check_password(contrasenya):
                auth_login(request, user)
                return redirect('inici')
            else:
                return redirect('login_error')

        except User.DoesNotExist:
            return redirect('login_error')

    return redirect('login_form')

def login_error(request):
    return render(request, 'login.html', {'error': 'Credenciales incorrectas'})

