from django.contrib import admin

# Register your models here.

from .models import *




@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id','cod', 'nombre', 'precio','stock','categoria']
    search_fields = ['nombre','cod']
    list_filter = ['precio','cod','nombre','stock','categoria']
    #list_editable = ['precio','cod','nombre','stock','categoria']


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['id','fecha', 'cliente', 'num_Factura', 'producto', ]
    search_fields = ['num_Factura']
    list_filter = ['num_Factura']
    list_editable = ['fecha','producto']
