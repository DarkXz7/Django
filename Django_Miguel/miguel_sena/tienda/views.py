from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db import IntegrityError

# Create your views here.

#vistas basadas en funciones

def prueba(request):
    return HttpResponse("<h1 style=color:green>Hola mundoo</h1")


def index(request):
    #eturn HttpResponse("Este es el index...")
    return render(request,"index.html")

def saludar(request, apellido):
    print(f"Hola {apellido}")
    return HttpResponse(f"Hola {apellido}")


def suma(request,num1,num2):
    return HttpResponse(f"resultado: {num1+num2}")

def encuesta_form(request):
    return render(request,"formulario_encuesta.html")

def procesar_encuesta(request):
    nombre = request.Post.get("nombre")

    tiene_hambre = request.Post.get("hambre")

    return HttpResponse(f"Su nombre es: {nombre} y {tiene_hambre} tiene hambre")


def sumar_formulario(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))

        #return render(f"La suma de {n1} y {n2} es: {int(n1)+int(n2)}")
        contexto= {
            "num1": n1,
            "num2": n2,
            "respuesta": n1 + n2
            
        }
        
        return render(request, "sumar_respuesta.html", contexto)
    else:
        return render(request, "sumar_formulario.html")


#crud
def productos(request):
    #select * from producto
    q = Producto.objects.all()
    contexto = {
    "data": q
    }
    return render (request, "productos/listar_productos.html", contexto)

def eliminar_producto (request , id_producto):
    try:
        q = Producto.objects.get(pk = id_producto)
        q.delete()
        return HttpResponse("Producto eliminado Correctamente")
    except Producto.DoesNotExist:
        return HttpResponse("Error: El producto no existe")
    except IntegrityError:
        return HttpResponse ("no se puede el producto pq esta relacionado en facturas")
    except Exception as e:
        return HttpResponse (f"Error: {e}")
