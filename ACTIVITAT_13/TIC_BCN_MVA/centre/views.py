from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template)

def profe(request):
    professor = {"name":"Roger", "surname1":"Sobrino", "surname2":"Gil", "correu":"roger.sobrino@iticbcn.cat", "curs":"DAW2A", "tutor":True, "moduls": "M7"}
    template = loader.get_template('profesor.html')
    dades = template.render({'nombre':professor["name"], 'surname1':professor["surname1"], 'surname2':professor["surname2"], 'correu':professor["correu"],
                             'curs':professor["curs"], 'tutor':professor["tutor"], 'moduls':professor["moduls"]})
    return HttpResponse(dades)

def alumn(request):
    alumnat = {"name":"Milena", "surname1":"Vardumyan", "surname2":"Aleksanyan", "correu":"2023_milena.vardumyan@iticbcn.cat", "curs":"DAW2A", "moduls": ["M7", "M6", "M5"]}
    template = loader.get_template('students.html')
    dades = template.render({'nombre':alumnat["name"], 'surname1':alumnat["surname1"], 'surname2':alumnat["surname2"], 'correu':alumnat["correu"],
                             'curs':alumnat["curs"], 'moduls':alumnat["moduls"]})
    return HttpResponse(dades)