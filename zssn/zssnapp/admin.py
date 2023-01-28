from django.contrib import admin

from .models import Sobrevivente, Infectados, Item, Mercado, Inventario
# from crud_app.forms import descontoForm


@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "idade",
                    "sexo", "data_do_registro")
    list_display_links = ("nome",)
    fieldsets = (
        ('Dados do sobrevivente', {
            'classes': ('extrapretty'),
            'fields': ('nome', 'idade', 'sexo', 'lat', 'long')
        }),
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "valor", "data_do_registro")
    list_display_links = ("nome",)
    fieldsets = (
        ('Dados do Item', {
            'classes': ('extrapretty'),
            'fields': ('nome', 'valor')
        }),
    )