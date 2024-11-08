# Generated by Django 4.2.15 on 2024-10-16 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finanzasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idCompra', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCompra', models.DateField()),
                ('cantidadCompra', models.IntegerField()),
                ('valorCompra', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=255)),
                ('valorProducto', models.IntegerField()),
                ('cantidadTotal', models.IntegerField()),
                ('valorTotal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idProveedor', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProveedor', models.CharField(max_length=255)),
                ('telefonoProveedor', models.IntegerField()),
                ('direccionProveedor', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False)),
                ('fechaVenta', models.DateField()),
                ('cantidadVenta', models.IntegerField()),
                ('valorVenta', models.IntegerField()),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzasApp.producto')),
            ],
        ),
        migrations.DeleteModel(
            name='Proveedores',
        ),
        migrations.AddField(
            model_name='producto',
            name='idProveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzasApp.proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='idProducto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzasApp.producto'),
        ),
    ]
