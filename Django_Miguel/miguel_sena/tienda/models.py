from django.db import models

# Create your models here.
#ORM: mapeo de objetos relacionales
#Migrations - proceso de convertir una clase en tabla DB
#Models - es la tabla
#Registros - objeto
#campos - atributos de clase
#metodos: puedo calcular cosas, usarlos como campos

class Producto(models.Model):
    cod = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=254)
    precio = models.IntegerField()
    stock = models.IntegerField()
    CATEGORIAS = (
        (0,""),
        (1, 'Ropa'),
        (2, 'Comida'),
        (3, 'Electrodomésticos'),
    )
    categoria = models.IntegerField(choices=CATEGORIAS,default=0, null=True,blank=True)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.stock} unidades"

class Factura(models.Model):
    fecha = models.DateField(help_text="Fecha de factura YYYY-MM-DD")
    cliente = models.CharField(max_length=100)
    num_Factura = models.IntegerField()
    producto = models.ForeignKey('Producto', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.num_Factura} - {self.cliente} unidades"