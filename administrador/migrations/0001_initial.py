# Generated by Django 5.1.1 on 2024-11-23 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('importeTotal', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('cuotas', models.IntegerField(default=5)),
                ('cuotasRestantes', models.IntegerField(default=5)),
                ('importePagado', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('importeRestante', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=10)),
                ('cantidad', models.IntegerField(default=5)),
                ('lugarEntrega', models.CharField(blank=True, max_length=50, null=True)),
                ('fechaEntrega', models.CharField(blank=True, max_length=50, null=True)),
                ('horaEntrega', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.producto')),
                ('venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.venta')),
            ],
        ),
    ]
