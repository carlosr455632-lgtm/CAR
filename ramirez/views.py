from django.shortcuts import render

def inicio(request):
    return render(request, "ramirez/inicio.html")
from django.shortcuts import render

def inicio(request):
    return render(request, "ramirez/inicio.html")

def registro(request):
    return render (request, 'ramirez/formregistro.html')


def torneo_de_futbol(request):
    return render (request, 'ramirez/encuestasobredeportes.html')