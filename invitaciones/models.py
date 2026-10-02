from django.db import models

class Invitacion(models.Model):
    codigo = models.CharField(max_length=50, unique=True, help_text='Ej: FAM-01') # <-- NUEVO CAMPO
    nombre_grupo = models.CharField(max_length=150, help_text='Ej: Familia Maldonado Garza')
    mensaje_anecdota = models.TextField(blank=True, null=True)
    asistira = models.BooleanField(null=True, blank=True) 
    fecha_confirmacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre_grupo}"

class Invitado(models.Model):
    invitacion = models.ForeignKey(Invitacion, related_name='invitados', on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=100)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_completo

class SugerenciaCancion(models.Model):
    titulo_o_enlace = models.CharField(max_length=255)
    fecha_sugerencia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo_o_enlace