from django.db import models

# sobrevivente
#   id, nome, idade, sexo e ultimo local(latitude e longitude)
class Sobrevivente(models.Model):
    

# infectados (se tiver 3 denuncias o inventario é bloqueado e sobrevivente é considerado contaminado)
#   id, chave estrangeira(id do suspeito), quantidade de denuncias

# mercado
#   id, chave estrangeira(id do item de troca), chave estrangeira(id do item a ser trocado), quantidade da troca, quantidade do item a ser trocado

# inventario (so é possivel alterar por meio de negociação)
#   agua = 4
#   alimentacao = 3
#   medicação = 2
#   munição = 1
#   id, quantidade, valor unitario



