from django.shortcuts import render
from .models import RegistroAsistencia

def lista_asistencia(request):
    registros = RegistroAsistencia.objects.all()
    return render(request, 'asistencia/lista.html', {'registros': registros})