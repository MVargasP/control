from rest_framework import serializers
#from apps.cliente.models import Cliente



class ClienteSerializer(serializers.Serializer):
    documento = serializers.FileField()
    fecha_inicio_tarjeta = serializers.DateField()   
    fecha_fin_tarjeta = serializers.DateField()   
  