from django.views.generic import TemplateView
from django.views.generic.list import ListView
from rest_framework import generics

from .models import Sobrevivente, Mercado, ItensInventario, Item, GrupoItens, Infectados
from .serializers import SobreviventesSerializer, ItensInventarioSerializer, ItemSerializer,GrupoItensSerializer, InfectadosSerializer

class IndexView(TemplateView):
    template_name = "index.html"

class LoginView(TemplateView):
    template_name = "pages/Login.html"

class CadastroView(TemplateView):
    template_name = "pages/Cadastro.html"

class SobreviventesView(ListView):
    model = Sobrevivente
    fields = [
        'nome', 'idade', 'sexo', 'infectado', 'lat', 'long'
    ]
    template_name = "pages/Sobreviventes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sobreviventes'] = Sobrevivente.objects.all()
        return context

class RelatoriosView(TemplateView):
    template_name = "pages/Relatorios.html"

class MercadoView(ListView):
    model = Mercado
    fields = [
        'sobrevivente_negociador', 'sobrevivente_receptor', 'item_troca', 'item_a_trocar', 'quant_itens_troca', 'quant_itens_a_trocar'
    ]
    template_name = "pages/Mercado.html"


class SobreviventesListApi(generics.ListCreateAPIView):
    serializer_class = SobreviventesSerializer
    def get_queryset(self):
        queryset = Sobrevivente.objects.all()
        return queryset

class SobreviventesDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SobreviventesSerializer
    queryset = Sobrevivente.objects.all()


class ItensInventarioListApi(generics.ListCreateAPIView):
    serializer_class = ItensInventarioSerializer
    def get_queryset(self, **kwargs):
        queryset = ItensInventario.objects.all()
        print(**kwargs)
        return queryset

class ItensInventarioDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItensInventarioSerializer
    def get_queryset(self):
        queryset = ItensInventario.objects.all()
        return queryset


class ItensListApi(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset

class ItensDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class GrupoItensListApi(generics.ListCreateAPIView):
    serializer_class = GrupoItensSerializer
    def get_queryset(self):
        queryset = GrupoItens.objects.all()
        return queryset

class GrupoItensDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GrupoItensSerializer
    queryset = GrupoItens.objects.all()


class InfectadosListApi(generics.ListCreateAPIView):
    serializer_class = InfectadosSerializer
    def get_queryset(self):
        queryset = Infectados.objects.all()
        return queryset

class InfectadosDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InfectadosSerializer
    queryset = Infectados.objects.all()







