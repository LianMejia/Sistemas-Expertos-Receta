from interfaz.forms import IngredientesForm
from django.shortcuts import redirect, render
from interfaz.models import ingredientes
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def menuPrincipal(request):
    return render(request, 'inicio.html')

def ingresoIngredientes(request):
    queryset = request.GET.get("buscar")
    posts = ingredientes.objects.all()
    if queryset:
        posts = ingredientes.objects.filter(
            Q(ingrediente1__icontains = queryset) |
            Q(ingrediente2__icontains = queryset) |
            Q(ingrediente3__icontains = queryset) |
            Q(ingrediente4__icontains = queryset) |
            Q(ingrediente5__icontains = queryset)
        ).distinct()
    return render(request, 'ingredientes.html', {'posts': posts, 'queryset':queryset})
    #ingredientes_no = ingredientes.objects.count()

def ingresoNombreIngredientes(request):
    queryset = request.GET.get("buscar")
    posts = ingredientes.objects.all()
    if queryset:
        posts = ingredientes.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()
    return render(request, 'nombre_ingrediente.html', {'posts': posts, 'queryset': queryset})

def detalleProducto(request, id):
    detalleIngrediente = ingredientes.objects.get(pk=id)
    return render(request, 'detalle_recetas.html', {'dReceta': detalleIngrediente})

def listaIngredientes(request):
    posts = ingredientes.objects.all()
    return render(request, 'lista_ingredientes.html', {'posts': posts})

#def inforecetas(request):
    return render(request, 'recetas.html')