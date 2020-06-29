from builtins import set
from rest_framework import serializers
from api import models



class TelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Telefono
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Persona
        fields = '__all__'
