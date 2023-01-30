from django.views.generic import TemplateView
from django.views.generic.list import ListView
from rest_framework import generics

from .models import Sobrevivente, Mercado, Inventario
from .serializers import SobreviventesSerializer

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
        context['inventario'] = Inventario.objects.all()
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