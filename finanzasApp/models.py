from django.db import models


# Modelo para Proveedores
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombreProveedor = models.CharField(max_length=255)
    telefonoProveedor = models.IntegerField()
    direccionProveedor = models.CharField(max_length=255)


# Modelo para Productos
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=255)
    valorProducto = models.IntegerField()
    cantidadTotal = models.IntegerField()
    valorTotal = models.IntegerField()  
    idProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        # Calcula el valor total antes de guardar
        self.valorTotal = self.valorProducto * self.cantidadTotal
        super().save(*args, **kwargs)


# Modelo para Compras
class Compra(models.Model):
    idCompra = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaCompra = models.DateField()
    cantidadCompra = models.IntegerField()
    valorCompra = models.IntegerField()
    
    def save(self, *args, **kwargs):
        # Calcula el valor de la compra antes de guardar
        self.valorCompra = self.cantidadCompra * self.idProducto.valorProducto
        super().save(*args, **kwargs)


# Modelo para Ventas
class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fechaVenta = models.DateField()
    cantidadVenta = models.IntegerField()
    valorVenta = models.IntegerField()
    
    def save(self, *args, **kwargs):
        # Calcula el valor de la venta antes de guardar
        self.valorVenta = self.cantidadVenta * self.idProducto.valorProducto
        super().save(*args, **kwargs)



    