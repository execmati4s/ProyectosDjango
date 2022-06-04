from django.urls import path
from .views import index, donacion, Carrito, Gato, Perro, tarjeta, todos, listar, modificar, agregar, eliminarProducto, modificarProducto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('donacion/', donacion, name='donacion'),
    path('Carrito/', Carrito, name='Carrito'),
    path('Gato/', Gato, name='Gato'),
    path('Perro/', Perro, name='Perro'),
    path('tarjeta/', tarjeta, name='tarjeta'),
    path('todos/', todos, name='todos'),
    path('listar/', listar, name='listar'), 
    path('modificar/', modificar, name='modificar'), 
    path('agregar/', agregar, name="agregar"),
    path('eliminarProducto /<idProducto>', eliminarProducto, name="eliminarProducto"),
    path('modificarProducto/<idProducto>', modificarProducto, name="modificarProducto"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)