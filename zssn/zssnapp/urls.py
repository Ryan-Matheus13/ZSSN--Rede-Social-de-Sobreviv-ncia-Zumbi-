from django.urls import path
from .views import IndexView, LoginView, CadastroView, SobreviventesView, RelatoriosView, MercadoView, SobreviventesListApi, SobreviventesDetailApi, ItensInventarioListApi, ItensInventarioDetailApi, ItensListApi, ItensDetailApi, GrupoItensListApi, GrupoItensDetailApi

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('sobreviventes', SobreviventesView.as_view(), name='sobreviventes'),
    path('relatorios', RelatoriosView.as_view(), name='relatorios'),
    path('mercado', MercadoView.as_view(), name='mercado'),

    path('api/sobreviventes', SobreviventesListApi.as_view()),
    path('api/sobreviventes/<int:pk>/', SobreviventesDetailApi.as_view()),

    # itens inventario
    path('api/itens-inventario', ItensInventarioListApi.as_view()),
    path('api/itens-inventario/<int:pk>/', ItensInventarioDetailApi.as_view()),

    # itens
    path('api/itens', ItensListApi.as_view()),
    path('api/itens/<int:pk>/', ItensDetailApi.as_view()),

    # grupo de itens
    path('api/grupo-itens', GrupoItensListApi.as_view()),
    path('api/grupo-itens/<int:pk>/', GrupoItensDetailApi.as_view()),
]
