from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def profe(request):
    professor = {"name":"Roger", "surname1":"Sobrino", "surname2":"Gil", "correu":"roger.sobrino@iticbcn.cat", "curs":"DAW2A", "tutor":"si", "moduls":}
    template = loader.get_template('index_centre.html')
    dades = template.render({'nombre':professor["name"], 'surname1':professor["surname1"], 'surname2':professor["surname2"], 'age':professor["age"]})
    return HttpResponse(dades)