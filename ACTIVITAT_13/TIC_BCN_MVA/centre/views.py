from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'index.html')

def profe(request):
    professor = {
        'profe1': {
            "name":"Roger",
            "surname1":"Sobrino",
            "surname2":"Gil",
            "correu":"roger.sobrino@iticbcn.cat",
            "curs":["DAW2A", "DAM2B"],
            "tutor":True,
            "moduls": "M7"
        },
        'profe2':{
            "name":"Josep Oriol",
            "surname1": "Roca",
            "surname2": "Fabra",
            "correu": "joseporiol.roca@iticbcn.cat",
            "curs": ["DAW2B", "DAW2A", "DAW1A"],
            "tutor":True,
            "moduls": "M8"
        },
        'profe3': {
            "name": "Juan Manuel",
            "surname1": "Sánchez",
            "surname2": "Bel",
            "correu": "juanmanuel.sanchez@iticbcn.cat",
            "curs": ["DAW2B", "DAW2A"],
            "tutor": True,
            "moduls": "M6"
        }

    }
    context = {"profes": professor}
    return render(request, 'profesor.html', context)

def alumn(request):
    alumnat = {
        'alumne1': {
            "name": "Hugo",
            "surname1": "Sansegundo",
            "surname2": "Costantini",
            "correu": "2023_hugo.sansegundo@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M06", "M07", "M08", "ML"]
        },
        'alumne2': {
            "name": "Adrián",
            "surname1": "Navarro",
            "surname2": "Pérez",
            "correu": "2023_adrian.navarro@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M06", "M07", "M08", "Cloud"]
        },
        'alumne3': {
            "name": "Xavi",
            "surname1": "Porras",
            "surname2": "del Pino",
            "correu": "2023_xavier.porras@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M06", "M07", "M08"]
        },
        'alumne4': {
            "name": "Javier",
            "surname1": "Giménez",
            "surname2": "Sánchez",
            "correu": "2023_javier.gimenez@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M8"]
        },
        'alumne5': {
            "name": "Milena",
            "surname1": "Vardumyan",
            "surname2": "Aleksanyan",
            "correu": "2023_milena.vardumyan@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M013", "Big Data"]
        },
        'alumne6': {
            "name": "Daniel",
            "surname1": "Vallespin",
            "surname2": "Mellado",
            "correu": "2023_daniel.vallespin@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M8"]
        },
        'alumne7': {
            "name": "Félix Bequet",
            "surname1": "Balbin",
            "surname2": "Silva",
            "correu": "2023_felix.balbin@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M8", "Big Data"]
        },
        'alumne8': {
            "name": "Victor Andrés",
            "surname1": "Fernández",
            "surname2": "Álvarez",
            "correu": "2023_victor.fernandez@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M8", "IA"]
        },
        'alumne9': {
            "name": "Lila",
            "surname1": "Díez",
            "surname2": "Zhou",
            "correu": "2023_lila.diez@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M8", "ML"]
        },
        'alumne10': {
            "name": "Arman",
            "surname1": "Mohammed",
            "surname2": "Akther",
            "correu": "2023_arman.mohammed@iticbcn.cat",
            "curs": "DAW2A",
            "moduls": ["M7", "M6", "M8"]
        }

    }
    context = {"alumn":alumnat}
    return render(request, 'students.html', context)

def alumn_profe(request, pk):
    alumn_profe_Obj = None
    for i in professor:
        if i['id'] == pk:
            alumn_profe_Obj = i
    return render(request, {'profes':alumn_profe_Obj})


# Create your views here.
def index (request):
    return HttpResponse("Hello")