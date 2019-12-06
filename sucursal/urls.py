from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar', views.agregar),
    path('editar/<int:almacen_id>', views.editar),
]
