from django.contrib import admin
from .models import Invitacion, Invitado, SugerenciaCancion

# Esta configuración hace que el panel se vea más organizado
class InvitadoInline(admin.TabularInline):
    model = Invitado
    extra = 1 # Cuántas filas vacías mostrar por defecto

class InvitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_grupo', 'asistira', 'fecha_confirmacion')
    inlines = [InvitadoInline]

# Registramos los modelos
admin.site.register(Invitacion, InvitacionAdmin)
admin.site.register(SugerenciaCancion)