from django.contrib import admin

from .models import CategoriaProducto, CategoriaEspecie, Producto

# Register your models here.c

admin.site.register(CategoriaProducto)
admin.site.register(CategoriaEspecie)
admin.site.register(Producto)


    