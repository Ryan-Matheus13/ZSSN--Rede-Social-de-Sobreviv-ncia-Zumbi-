from django.urls import path
from .views import IndexView, LoginView, CadastroView, SobreviventesView, RelatoriosView, MercadoView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('cadastro', CadastroView.as_view(), name='cadastro'),
    path('sobreviventes', SobreviventesView.as_view(), name='sobreviventes'),
    path('relatorios', RelatoriosView.as_view(), name='relatorios'),
    path('mercado', MercadoView.as_view(), name='mercado'),

    # path('cadastrar/cliente', ClienteCreate.as_view(), name='cadastrar-cliente'),
    # path('cadastrar/servico', ServicoCreate.as_view(), name='cadastrar-servico'),
    # path('cadastrar/atendimento', AtendimentoCreate.as_view(), name='cadastrar-atendimento'),

    # path('editar/cliente/<int:pk>', ClienteUpdate.as_view(), name='editar-cliente'),
    # path('editar/servico/<int:pk>', ServicoUpdate.as_view(), name='editar-servico'),
    # path('editar/atendimento/<int:pk>', AtendimentoUpdate.as_view(), name='editar-atendimento'),

    # path('deletar/cliente/<int:pk>', ClienteDelete.as_view(), name='deletar-cliente'),
    # path('deletar/servico/<int:pk>', ServicoDelete.as_view(), name='deletar-servico'),
    # path('deletar/atendimento/<int:pk>', AtendimentoDelete.as_view(), name='deletar-atendimento'),

    # path('listar/cliente/', ClienteList.as_view(), name='listar-cliente'),
    # path('listar/servico/', ServicoList.as_view(), name='listar-servico'),
    # path('listar/atendimento/', AtendimentoList.as_view(), name='listar-atendimento'),
]