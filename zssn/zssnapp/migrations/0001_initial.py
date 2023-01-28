# Generated by Django 4.1.5 on 2023-01-28 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('valor', models.IntegerField(max_length=1)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sobrevivente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('idade', models.IntegerField(max_length=3)),
                ('sexo', models.CharField(max_length=20)),
                ('lat', models.DecimalField(decimal_places=4, max_digits=7)),
                ('long', models.DecimalField(decimal_places=4, max_digits=7)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant_itens_troca', models.IntegerField(max_length=11)),
                ('quant_itens_a_trocar', models.IntegerField(max_length=11)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
                ('fk_sobrevivente_negociador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sobreviventeNegociador', to='zssnapp.sobrevivente')),
                ('fk_sobrevivente_receptor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sobreviventeReceptor', to='zssnapp.sobrevivente')),
                ('item_a_trocar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itemATrocar', to='zssnapp.item')),
                ('item_troca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='itemTroca', to='zssnapp.item')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.IntegerField(max_length=1)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
                ('fk_sobrevivente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventarioDoSobrevivente', to='zssnapp.sobrevivente')),
            ],
        ),
        migrations.CreateModel(
            name='Infectados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denuncias', models.IntegerField(max_length=1)),
                ('data_do_registro', models.DateTimeField(auto_now_add=True)),
                ('fk_sobrevivente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='infectedSurvival', to='zssnapp.sobrevivente')),
            ],
        ),
    ]