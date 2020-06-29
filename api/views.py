from rest_framework import status, generics
from api import models
from api import serializers

class UserList(generics.ListCreateAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer

class UserTelefonos(generics.ListCreateAPIView):
    serializer_class = serializers.TelefonoSerializer
    def get_queryset(self):
        id = self.kwargs['userid']
        #print("Codigoooooooooo",id)
        return models.Telefono.objects.filter(persona_fk_id=id)



class TelefonoList(generics.ListCreateAPIView):
    queryset = models.Telefono.objects.all()
    serializer_class = serializers.TelefonoSerializer

class TelefonoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Telefono.objects.all()
    serializer_class = serializers.TelefonoSerializer