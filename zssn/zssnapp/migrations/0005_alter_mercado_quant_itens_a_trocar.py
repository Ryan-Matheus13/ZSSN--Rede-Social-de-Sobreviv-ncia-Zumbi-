# Generated by Django 4.1.5 on 2023-01-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zssnapp', '0004_grupoitens_remove_item_valor_item_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercado',
            name='quant_itens_a_trocar',
            field=models.IntegerField(null=True),
        ),
    ]
