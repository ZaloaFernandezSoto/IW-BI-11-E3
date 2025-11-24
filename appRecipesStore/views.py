from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta, TipoPlato, Ingrediente
from .forms import RecetaForm

# Create your views here.
def home(request):
    # Una receta por tipo de plato (por ejemplo, la más rápida)
    tipos = TipoPlato.objects.all()
    recetas_destacadas = []
    for tipo in tipos:
        receta = tipo.recetas.order_by('tiempo_preparacion').first()
        if receta:
            recetas_destacadas.append(receta)
    return render(request, 'appRecipesStore/index.html', {'recetas': recetas_destacadas})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'appRecipesStore/lista_recetas.html', {'recetas': recetas})

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'appRecipesStore/detalle_receta.html', {'receta': receta})

def lista_tipos_plato(request):
    tipos = TipoPlato.objects.all()
    return render(request, 'appRecipesStore/lista_tipos_plato.html', {'tipos': tipos})

def detalle_tipo_plato(request, pk):
    tipo = get_object_or_404(TipoPlato, pk=pk)
    return render(request, 'appRecipesStore/detalle_tipo_plato.html', {'tipo': tipo})

def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'appRecipesStore/lista_ingredientes.html', {'ingredientes': ingredientes})

def detalle_ingrediente(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    return render(request, 'appRecipesStore/detalle_ingrediente.html', {'ingrediente': ingrediente})

def crear_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()

    return render(request, 'appRecipesStore/crear_receta.html', {'form': form})
