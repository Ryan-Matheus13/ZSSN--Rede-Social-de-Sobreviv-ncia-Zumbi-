from django.contrib import admin

from .models import Sobrevivente, Infectados, Item, Mercado, Inventario, GrupoItens


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "idade",
                    "sexo", "data_do_registro")
    list_display_links = ("nome",)
    fieldsets = (
        ('Dados do sobrevivente', {
            'classes': ('extrapretty'),
            'fields': ('nome', 'infectado', 'idade', 'sexo', 'lat', 'long')
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


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ("id", "get_nome", "tamanho", "data_do_registro")
    list_display_links = ("get_nome",)
    fieldsets = (
        ('Dados do Grupo', {
            'classes': ('extrapretty'),
            'fields': ('sobrevivente', 'tamanho')
        }),
    )

    def get_nome(self, obj):
        return obj.sobrevivente.nome
    get_nome.admin_order_field = 'sobrevivente'
    get_nome.short_description = 'sobrevivente'


@admin.register(Mercado)
class MercadoAdmin(admin.ModelAdmin):
    list_display = ("id", "get_nome_comprador", "get_nome_vendedor", "get_nome_item_comprado", "get_nome_item_vendido", "quant_itens_troca", "quant_itens_a_trocar", "data_do_registro")
    list_display_links = ("id",)
    fieldsets = (
        ('Dados do Grupo', {
            'classes': ('extrapretty'),
            'fields': ('sobrevivente_negociador', 'sobrevivente_receptor', 'item_troca', 'item_a_trocar', 'quant_itens_troca', 'quant_itens_a_trocar')
        }),
    )

    def get_nome_comprador(self, obj):
        return obj.sobrevivente_negociador.nome
    get_nome_comprador.admin_order_field = 'sobrevivente_negociador'
    get_nome_comprador.short_description = 'comprador'

    def get_nome_vendedor(self, obj):
        return obj.sobrevivente_receptor.nome
    get_nome_vendedor.admin_order_field = 'sobrevivente_receptor'
    get_nome_vendedor.short_description = 'vendedor'

    def get_nome_item_comprado(self, obj):
        return obj.item_troca.nome
    get_nome_item_comprado.admin_order_field = 'item_troca'
    get_nome_item_comprado.short_description = 'item comprado'

    def get_nome_item_vendido(self, obj):
        return obj.item_a_trocar.nome
    get_nome_item_vendido.admin_order_field = 'item_a_trocar'
    get_nome_item_vendido.short_description = 'item vendido'
