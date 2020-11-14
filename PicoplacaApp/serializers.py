from rest_framework import serializers
from PicoplacaApp.models import Ciudades, Picoplaca

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = ('CiudadId',
                  'CiudadNombre')

class PicoplacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picoplaca
        fields = ('DigitoplacaId',
                  'DiaSemana',
                  'Ciudad',
                  'FechaEntrada',
                  'PhotoFileName')
