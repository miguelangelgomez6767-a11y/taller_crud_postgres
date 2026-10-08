from django.db import models

class RegistroAsistencia(models.Model):

    tipo_documento = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.fecha}"