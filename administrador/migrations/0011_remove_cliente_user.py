# Generated by Django 5.1.1 on 2024-11-30 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0010_cliente_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='user',
        ),
    ]
