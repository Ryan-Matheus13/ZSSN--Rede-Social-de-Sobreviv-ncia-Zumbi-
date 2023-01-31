from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.forms import ValidationError

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

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class ItensInventario(models.Model):

    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="item")
    quantidade = models.CharField(max_length=10)

    data_do_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.nome}' + f' - {self.quantidade}X'


class Sobrevivente(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=20)
    token = models.CharField(max_length=6, null=True, unique=True)
    itens_inventario = models.ManyToManyField(ItensInventario)
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


class Infectados(models.Model):

    id = models.AutoField(primary_key=True)
    sobrevivente = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="infectedSurvival")
    denuncias = models.IntegerField()

    data_do_registro = models.DateTimeField(auto_now_add=True)


class Mercado(models.Model):

    id = models.AutoField(primary_key=True)
    sobrevivente_comprador = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL, null=True, blank=True, related_name="sobreviventeComprador")
    item_comprado = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="itemComprado")
    quant_itens_compra = models.IntegerField(null=True)

    sobrevivente_vendedor = models.ForeignKey(
        Sobrevivente, on_delete=models.SET_NULL,null=True, blank=True, related_name="sobreviventeVendendor")
    item_vendido = models.ForeignKey(
        Item, on_delete=models.SET_NULL, null=True, blank=True, related_name="itemVendido")
    quant_itens_venda = models.IntegerField()

    data_do_registro = models.DateTimeField(auto_now_add=True)


