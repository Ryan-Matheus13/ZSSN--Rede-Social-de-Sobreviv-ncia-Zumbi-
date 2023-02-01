from rest_framework import serializers
from .models import Sobrevivente, ItensInventario, Item, GrupoItens, Infectados

class SobreviventesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sobrevivente
        fields = ('__all__')

class InfectadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infectados
        fields = ('__all__')

class ItensInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensInventario
        fields = ('__all__')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')

class GrupoItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoItens
        fields = ('__all__')
