from django.http.response import HttpResponse
from django.shortcuts import render

def ejemplo_view (request):
    variable = "Hola desde la vista"
    return render(request, 'ejemplo.html', locals())
