# Generated by Django 5.1.1 on 2024-12-01 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0017_venta_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
    ]
