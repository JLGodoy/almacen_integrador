from django.forms import ModelForm
from .models import Almacenes


class AlmacenesForm(ModelForm):
    class Meta:
        model = Almacenes
        fields = ['IdAlmacen', 'NombreAlmacen', 'Ubicacion', 'IdEstatus']