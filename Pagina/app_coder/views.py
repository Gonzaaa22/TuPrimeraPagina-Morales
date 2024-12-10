from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .models import Categoria

def index(request):
    return render(request, 'app_coder/index.html')

def agregar_datos(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        
        if producto_form.is_valid():
            producto_form.save()
            return redirect('index')

    else:
        producto_form = ProductoForm()
        cliente_form = ClienteForm()

    categorias = Categoria.objects.all()
    return render(request, 'app_coder/agregar_datos.html', {'producto_form': producto_form, 'cliente_form': cliente_form, 'categorias': categorias})

from django.shortcuts import render
from .models import Producto

def buscar_producto(request):
    query = request.GET.get('q', '') 
    productos = Producto.objects.filter(nombre__icontains=query) if query else [] 
    return render(request, 'app_coder/buscar_producto.html', {
        'query': query,
        'productos': productos
    })

