from django.urls import path
from .views import IndexView, LoginView, CadastroView, SobreviventesView, RelatoriosView, MercadoView, SobreviventesListApi, SobreviventesDetailApi

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('sobreviventes', SobreviventesView.as_view(), name='sobreviventes'),
    path('relatorios', RelatoriosView.as_view(), name='relatorios'),
    path('mercado', MercadoView.as_view(), name='mercado'),

    path('api/sobreviventes', SobreviventesListApi.as_view()),
    path('api/sobreviventes/<int:pk>/', SobreviventesDetailApi.as_view()),

]
