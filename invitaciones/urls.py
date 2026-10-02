from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvitacionViewSet, InvitadoViewSet, SugerenciaCancionViewSet

router = DefaultRouter()
router.register(r'invitaciones', InvitacionViewSet)
router.register(r'invitados', InvitadoViewSet)
router.register(r'canciones', SugerenciaCancionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]