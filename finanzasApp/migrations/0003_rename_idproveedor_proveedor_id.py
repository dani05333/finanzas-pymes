# Generated by Django 4.2.15 on 2024-11-01 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanzasApp', '0002_compra_producto_proveedor_venta_delete_proveedores_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='idProveedor',
            new_name='id',
        ),
    ]