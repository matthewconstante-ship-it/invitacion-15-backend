from rest_framework import serializers
from .models import Invitacion, Invitado, SugerenciaCancion

class InvitadoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False) # Para identificar al invitado existente

    class Meta:
        model = Invitado
        fields = ['id', 'nombre_completo', 'confirmado']

class InvitacionSerializer(serializers.ModelSerializer):
    invitados = InvitadoSerializer(many=True)

    class Meta:
        model = Invitacion
        fields = ['id', 'codigo', 'nombre_grupo', 'mensaje_anecdota', 'asistira', 'invitados']

    def update(self, instance, validated_data):
        invitados_data = validated_data.pop('invitados', [])
        
        # Actualizamos datos principales del grupo
        instance.nombre_grupo = validated_data.get('nombre_grupo', instance.nombre_grupo)
        instance.asistira = validated_data.get('asistira', instance.asistira)
        instance.save()

        # Actualizamos el estado "confirmado" de cada invitado de la familia
        for invitado_data in invitados_data:
            invitado_id = invitado_data.get('id')
            if invitado_id:
                invitado = Invitado.objects.get(id=invitado_id, invitacion=instance)
                invitado.confirmado = invitado_data.get('confirmado', invitado.confirmado)
                invitado.save()

        return instance

class SugerenciaCancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SugerenciaCancion
        fields = '__all__'