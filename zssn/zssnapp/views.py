from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from rest_framework import viewsets
from rest_framework import permissions
from zssnapp.serializers import UserSerializer, GroupSerializer

from .models import Sobrevivente, Mercado

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

class RelatoriosView(TemplateView):
    template_name = "pages/Relatorios.html"

class MercadoView(TemplateView):
    template_name = "pages/Mercado.html"

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]