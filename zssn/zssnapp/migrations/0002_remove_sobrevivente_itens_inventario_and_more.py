# Generated by Django 4.1.5 on 2023-01-31 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zssnapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sobrevivente',
            name='itens_inventario',
        ),
        migrations.AddField(
            model_name='itensinventario',
            name='sobrevivente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item', to='zssnapp.sobrevivente'),
        ),
    ]
