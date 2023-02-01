from django.contrib import admin

from .models import Sobrevivente, Infectados, Item, Mercado, GrupoItens, ItensInventario


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "idade",
                    "sexo", "data_do_registro")
    list_display_links = ("nome",)
    fieldsets = (
        ('Dados do sobrevivente', {
            'classes': ('extrapretty'),
            'fields': ('nome', 'token', 'infectado', 'idade', 'sexo', 'lat', 'long')
        }),
    )


@admin.register(Infectados)
class InfectadosAdmin(admin.ModelAdmin):
    list_display = ("id", "get_nome", "denuncias", "data_do_registro")
    list_display_links = ("get_nome",)
    fieldsets = (
        ('Dados do Infectados', {
            'classes': ('extrapretty'),
            'fields': ('sobrevivente', 'denuncias')
        }),
    )

    def get_nome(self, obj):
        return obj.sobrevivente.nome
    get_nome.admin_order_field = 'sobrevivente'
    get_nome.short_description = 'sobrevivente'


@admin.register(ItensInventario)
class ItensInventarioAdmin(admin.ModelAdmin):
    list_display = ("id", "item", "quantidade", "sobrevivente",
     "get_total")
    list_display_links = ("item",)
    fieldsets = (
        ('Dados do Item', {
            'classes': ('extrapretty'),
            'fields': ('item', 'quantidade', 'sobrevivente')
        }),
    )

    def get_total(self, obj):
        quant = obj.quantidade 
        valor = obj.item.grupo.valor
        total = int(quant) * int(valor)
        return f'{total} Slots'
    get_total.admin_order_field = 'item'
    get_total.short_description = 'total'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "grupo", "get_valor", "data_do_registro")
    list_display_links = ("nome",)
    fieldsets = (
        ('Dados do Item', {
            'classes': ('extrapretty'),
            'fields': ('nome', 'grupo')
        }),
    )

    def get_valor(self, obj):
        return obj.grupo.valor
    get_valor.admin_order_field = 'grupo'
    get_valor.short_description = 'Valor'


@admin.register(GrupoItens)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "valor", "data_do_registro")
    list_display_links = ("nome",)
    fieldsets = (
        ('Dados do Grupo', {
            'classes': ('extrapretty'),
            'fields': ('nome', 'valor')
        }),
    )


@admin.register(Mercado)
class MercadoAdmin(admin.ModelAdmin):
    list_display = ("id", "get_nome_comprador", "get_nome_vendedor", "get_nome_item_comprado", "get_nome_item_vendido", "quant_itens_compra", "quant_itens_venda", "data_do_registro")
    list_display_links = ("id",)
    fieldsets = (
        ('Dados do Grupo', {
            'classes': ('extrapretty'),
            'fields': ('sobrevivente_comprador', 'sobrevivente_vendedor', 'item_compra', 'item_venda', 'quant_itens_compra', 'quant_itens_venda')
        }),
    )

    def get_nome_comprador(self, obj):
        return obj.sobrevivente_comprador.nome
    get_nome_comprador.admin_order_field = 'sobrevivente_comprador'
    get_nome_comprador.short_description = 'comprador'

    def get_nome_vendedor(self, obj):
        return obj.sobrevivente_vendedor.nome
    get_nome_vendedor.admin_order_field = 'sobrevivente_vendedor'
    get_nome_vendedor.short_description = 'vendedor'

    def get_nome_item_comprado(self, obj):
        return obj.item_compra.nome
    get_nome_item_comprado.admin_order_field = 'item_compra'
    get_nome_item_comprado.short_description = 'item comprado'

    def get_nome_item_vendido(self, obj):
        return obj.item_venda.nome
    get_nome_item_vendido.admin_order_field = 'item_venda'
    get_nome_item_vendido.short_description = 'item vendido'
