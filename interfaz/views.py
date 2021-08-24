from interfaz.forms import IngredientesForm
from django.shortcuts import redirect, render
from interfaz.models import ingredientes
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def recetas(request):
    queryset = request.GET.get("buscar")
    posts = ingredientes.objects.all()
    if queryset:
        posts = ingredientes.objects.filter(
            Q(ingrediente1__icontains = queryset) |
            Q(ingrediente2__icontains = queryset) |
            Q(ingrediente3__icontains = queryset)
        ).distinct()
    return render(request, 'inicio.html', {'posts': posts})
    #ingredientes_no = ingredientes.objects.count()
    """ crear_ingrediente = ingredientes.objects.name('lechuga') """

    """ if request.method == 'POST':
        formIngredients = IngredientesForm(request.POST)
        if formIngredients.is_valid():
            formIngredients.save()
            return redirect('index')
    else:
        formIngredients = IngredientesForm() """

    """ return render(request, 'inicio.html', {'formIngredients': formIngredients}) """

def inforecetas(request):
    return render(request, 'recetas.html')