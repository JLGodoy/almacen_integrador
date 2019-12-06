from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sucursal_listado_url'),
    path('agregar', views.agregar, name="sucursal_agregar_url"),
    path('editar/<int:almacen_id>', views.editar, name="sucursal_editar_url"),
    path('baja/<int:almacen_id>', views.baja, name="sucursal_baja_url")
]
