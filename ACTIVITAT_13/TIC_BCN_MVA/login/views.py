from django.shortcuts import render
from .forms import PersonForm
# Create your views here.
def inici(request):
    return render(request, 'inici.html')

def user_form(request):
    form = PersonForm()
    context = {'form':form}
    return render(request, 'form.html', context)

