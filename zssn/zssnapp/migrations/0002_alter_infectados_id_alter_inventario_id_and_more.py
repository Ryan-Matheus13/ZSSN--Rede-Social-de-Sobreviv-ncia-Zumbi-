# Generated by Django 4.1.5 on 2023-01-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zssnapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infectados',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mercado',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sobrevivente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]