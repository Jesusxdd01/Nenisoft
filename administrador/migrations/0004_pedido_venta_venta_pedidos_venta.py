# Generated by Django 5.1.1 on 2024-11-23 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0003_remove_pedido_venta_remove_venta_pedidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='administrador.venta'),
        ),
        migrations.AddField(
            model_name='venta',
            name='pedidos_venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='administrador.pedido'),
        ),
    ]
