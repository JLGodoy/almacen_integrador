from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as log, update_session_auth_hash, logout as out
from django.views.generic import CreateView

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegistroForm, UCFconMail
from .models import usuario
from django.http import HttpResponse


def index (request):
    return HttpResponse(request.session.exists())
    if request.session:
        return render(request,"index.html")
    else:
        return render(request,'registration/login.html')

def loginpage (request):
    return render(request,'login.html')

def login (request):
    if request.method == "POST":
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            log(request, user)
            request.session['user'] = request.POST['username']
            return render(request,"index.html")
    return redirect('/')


def logout(request):
    out(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            log(request, user)
            return render(request,"index.html")

    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request,'registration/register.html', context)



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña cambiada con éxito')
            return redirect('/')
        else:
            messages.error(request, 'Error!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'registration/change_password.html', context)



class RegisterView(CreateView):
    model = User
    template_name= 'registration/register.html'
    form_class = RegistroForm
    succes_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
