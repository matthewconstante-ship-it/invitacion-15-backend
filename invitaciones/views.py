from rest_framework import viewsets
from .models import Invitacion, Invitado, SugerenciaCancion
from .serializers import InvitacionSerializer, InvitadoSerializer, SugerenciaCancionSerializer

class InvitacionViewSet(viewsets.ModelViewSet):
    queryset = Invitacion.objects.all()
    serializer_class = InvitacionSerializer
    lookup_field = 'codigo' # <-- Permite buscar por código en la URL (ej: /api/invitaciones/FAM-01/)

class InvitadoViewSet(viewsets.ModelViewSet):
    queryset = Invitado.objects.all()
    serializer_class = InvitadoSerializer

class SugerenciaCancionViewSet(viewsets.ModelViewSet):
    queryset = SugerenciaCancion.objects.all()
    serializer_class = SugerenciaCancionSerializer