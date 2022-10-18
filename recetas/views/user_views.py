from django.shortcuts import render

def registro(request):
    contexto = {}
    return render(request, "usuarios/registro.html", contexto)