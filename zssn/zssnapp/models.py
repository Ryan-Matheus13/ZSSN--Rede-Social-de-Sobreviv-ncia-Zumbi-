from django.db import models
from django.forms import ValidationError

# sobrevivente
#   id, nome, idade, sexo e ultimo local(latitude e longitude)


class Sobrevivente(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20)
    infectado = models.BooleanField(default=False, null=True)
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    long = models.DecimalField(max_digits=7, decimal_places=4)

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def clean(self):
        # validar valores de -90 a 90
        if self.lat < -90 or self.lat > 90:
            raise ValidationError("Valor de latitude é invalido, tente um valor entre (-90,0000,0000 e 90)")
        if self.long < -180 or self.long > 180:
            raise ValidationError("Valor de longitude é invalido, tente um valor entre (-180,0000 e 180,0000)")

# infectados (se tiver 3 denuncias o inventario é bloqueado e sobrevivente é considerado contaminado)
#   id, chave estrangeira(id do suspeito), quantidade de denuncias


class Infectados(models.Model):

    id = models.AutoField(primary_key=True)
    sobrevivente = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="infectedSurvival")
    denuncias = models.IntegerField()

    data_do_registro = models.DateTimeField(auto_now_add=True)


# item
#   id, nome, valor

class GrupoItens(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    valor = models.IntegerField()

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Item(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    grupo = models.ForeignKey(
        GrupoItens, on_delete=models.SET_NULL, null=True, blank=True, related_name="grupoItem")
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
    quant_itens_troca = models.IntegerField()
    quant_itens_a_trocar = models.IntegerField()
    sobrevivente_negociador = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="sobreviventeNegociador")
    sobrevivente_receptor = models.ForeignKey(
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
    sobrevivente = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="inventarioDoSobrevivente")
    tamanho = models.IntegerField()

    data_do_registro = models.DateTimeField(auto_now_add=True)
