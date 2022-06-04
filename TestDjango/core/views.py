from dataclasses import dataclass
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django. views. decorators. csrf import csrf_exempt

from core.forms import ProductoForm
from .models import Producto

from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def index(request):
    
    productos = Producto.objects.all()
    
    data = {
        'productos' : productos
    }
    
    return render(request, 'core/index.html', data)

def Carrito(request):
    return render(request, 'core/Carrito.html')

def donacion(request):
    return render(request, 'core/donacion.html')

def Gato(request):
    return render(request, 'core/Gato.html')

def Perro(request):
    return render(request, 'core/Perro.html')

def tarjeta(request):
    return render(request, 'core/tarjeta.html')

def todos(request):
    return render(request, 'core/todos.html')

@csrf_exempt
def modificar(request):
    return render(request, 'core/modificar.html')

@csrf_exempt
def listar(request):
    productosListado = Producto.objects.all()  
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productosListado,5)
        productosListado = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'entity' : productosListado,
        'paginator' : paginator
    }
    
    return render(request, 'core/listar.html', data)

@csrf_exempt
def agregar(request):
    datos= {
        'form' : ProductoForm()
    }  
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)    
        if formulario.is_valid:
            formulario.save()
            datos["mensaje"] = "guardado correctamente"
        else:
            datos["form"] = formulario
    
    return render(request, 'core/agregar.html', datos)

@csrf_exempt
def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(idProducto=idProducto)
    producto.delete()
    return redirect('/listar')



@csrf_exempt
def modificarProducto(request, idProducto):
    
    producto = get_object_or_404(Producto, idProducto=idProducto)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar')
        data["form"] = formulario
        
    return render(request,  'core/modificar.html', data)
    



#class Persona:
    #def __init__(self,nombre,edad):
        #self.nombre=nombre
       # self.edad=edad
        #super().__init__()

#def test(request):
    #lista=["lasaña","Charquican","Porotos verdes"]
    #hijo=Persona("JUANITO","10")
    #contexto={"nombre":"anita la huerfanita","comidas": lista, "hijo":hijo}
    #return render(request, 'core/test.html',contexto)
