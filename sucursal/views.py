from django.shortcuts import render, redirect
from .forms import AlmacenesForm
from .models import Almacenes
from django.template import loader
from django.http import HttpResponse

def index(request):
    latest_almacen_list = Almacenes.objects.order_by('-Ubicacion')[:5]
    template = loader.get_template('sucursal/index.html')
    context = {
        'latest_almacen_list': latest_almacen_list,
    }
    return HttpResponse(template.render(context, request))

def agregar(request):
    # Creamos un formulario vacío
    form = AlmacenesForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AlmacenesForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "sucursal/add.html", {'form': form})

def editar(request, almacen_id):
    # Recuperamos la instancia
    instancia = Almacenes.objects.get(IdAlmacen=almacen_id)

    # Creamos el formulario con los datos de la instancia
    form = AlmacenesForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = AlmacenesForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "sucursal/edit.html", {'form': form})
