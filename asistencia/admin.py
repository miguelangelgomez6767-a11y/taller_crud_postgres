from django.contrib import admin
from .models import RegistroAsistencia

@admin.register(RegistroAsistencia)
class RegistroAsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_documento', 'documento', 'nombres', 'apellidos', 'whatsapp', 'fecha', 'asistio')
    list_filter = ('asistio', 'fecha')
    search_fields = ('documento', 'nombres', 'apellidos')
