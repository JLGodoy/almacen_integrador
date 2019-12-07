from django.forms import ModelForm
from .models import Roles
from .models import PermisosAsignados

class RolesForm(ModelForm):
    class Meta:
        model = Roles
        fields = ['IdRol', 'NombreRol', 'IdEstatus']

class PermisosasignadosForm(ModelForm):
    class Meta:
        model = PermisosAsignados
        fields = ['IdPermisoAsignado', 'IdUsuario', 'IdPermiso', 'IdEstatus'] 