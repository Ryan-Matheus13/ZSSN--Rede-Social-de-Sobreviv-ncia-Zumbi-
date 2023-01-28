from django.db import models

# sobrevivente
#   id, nome, idade, sexo e ultimo local(latitude e longitude)


class Sobrevivente(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    idade = models.IntegerField(max_length=3)
    sexo = models.CharField(max_length=20)
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    long = models.DecimalField(max_digits=7, decimal_places=4)

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# infectados (se tiver 3 denuncias o inventario é bloqueado e sobrevivente é considerado contaminado)
#   id, chave estrangeira(id do suspeito), quantidade de denuncias


class Infectados(models.Model):

    id = models.AutoField(primary_key=True)
    fk_sobrevivente = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="infectedSurvival")
    denuncias = models.IntegerField(max_length=1)

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sobrevivente

# item
#   id, nome, valor

class GrupoItens(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    valor = models.IntegerField(max_length=1)

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Item(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    grupo = models.ForeignKey(
        GrupoItens, on_delete=models.SET_NULL, null=True, blank=True, related_name="itemATrocar")
    # valor = models.IntegerField(max_length=1)

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# mercado
#   id, chave estrangeira(id do item de troca), chave estrangeira(id do item a ser trocado), quantidade da troca, quantidade do item a ser trocado


class Mercado(models.Model):

    id = models.AutoField(primary_key=True)
    item_troca = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="itemTroca")
    item_a_trocar = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="itemATrocar")
    quant_itens_troca = models.IntegerField(max_length=11)
    quant_itens_a_trocar = models.IntegerField(max_length=11)
    fk_sobrevivente_negociador = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="sobreviventeNegociador")
    fk_sobrevivente_receptor = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="sobreviventeReceptor")

    data_do_registro = models.DateTimeField(auto_now_add=True)


# inventario (so é possivel alterar por meio de negociação)
#   agua = 4
#   alimentacao = 3
#   medicação = 2
#   munição = 1
#   id, id_sobrevivente, quantidade
class Inventario(models.Model):

    id = models.AutoField(primary_key=True)
    fk_sobrevivente = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="inventarioDoSobrevivente")
    quant = models.IntegerField(max_length=1)

    data_do_registro = models.DateTimeField(auto_now_add=True)
