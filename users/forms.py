from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    """Formulario personalizado para el registro de usuarios """

    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]
        labels = {
            'username' : 'Username',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Correo',
            'password' : 'Contraseña',
            }
class UCFconMail(UserCreationForm):
    username = forms.CharField(max_length = 20, required = True)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    email = forms.EmailField(max_length = 50, required = True)

    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        ]
