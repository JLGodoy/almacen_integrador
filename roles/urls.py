from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='roles_listado_url'),
    path('agregar', views.agregar, name="roles_agregar_url"),
    path('editar/<int:rol_id>', views.editar, name="roles_editar_url"),
    path('baja/<int:rol_id>', views.baja, name="roles_baja_url")
]
