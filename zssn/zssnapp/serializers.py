from rest_framework import serializers
from .models import Sobrevivente

class SobreviventesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ('__all__')