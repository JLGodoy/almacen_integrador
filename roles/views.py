from django.shortcuts import render, redirect
from .forms import RolesForm
from .models import Roles, Permisos
from django.template import loader
from django.http import HttpResponse

def index(request):
    latest_roles_list = Roles.objects.order_by('-NombreRol')
    template = loader.get_template('roles/index.html')
    context = {
        'latest_roles_list': latest_roles_list,
    }
    return HttpResponse(template.render(context, request))

def agregar(request):
    # Creamos un formulario vacío
    form = RolesForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = RolesForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            instancia.IdEstatus = 1
            # Podemos guardarla cuando queramos
            instancia.save()

            # if request.POST.usuariosListado:
            #     form = PermisosasignadosForm()
            #     instancia2 = form.save(commit=False)
            #     instancia2.IdUsuario
            #     instancia2.IdPermiso = 1
            #     instancia2.IdEstatus = 1

            # Después de guardar redireccionamos a la lista
            return redirect('/roles')

    # Si llegamos al final renderizamos el formulario
    permisos_list = Permisos.objects.order_by('-NombrePermiso')
    return render(request, "roles/add.html", {'form': form, 'permisos_list': permisos_list})

def editar(request, rol_id):
    # Recuperamos la instancia
    instancia = Roles.objects.get(IdRol=rol_id)

    # Creamos el formulario con los datos de la instancia
    form = RolesForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = RolesForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            return redirect('/roles')

    # Si llegamos al final renderizamos el formulario
    return render(request, "roles/edit.html", {'form': form})

def baja(request, rol_id):
    instancia = Roles.objects.get(IdRol=rol_id)

    form = RolesForm(instance=instancia)

    if request.method == "GET":
        instancia.IdEstatus = 1
        instancia.save()
        return redirect('/roles')


