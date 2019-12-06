from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as log, update_session_auth_hash, logout as out
from django.views.generic import CreateView

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegistroForm, UCFconMail
from .models import usuario
from django.http import HttpResponse
from django.contrib.sessions.models import Session


def index (request):
    if request.session.is_empty():
        return render(request,'registration/login.html') 
    return render(request,"dashboard.html")

def login (request):
    if request.method == "POST":
        #killSession(request)

        my_old_sessions = Session.objects.all()
        for row in my_old_sessions:
            if row.get_decoded().get("username") == request.POST['username']:
                row.delete()
        user = authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            log(request, user)
            request.session['username'] = request.POST['username']
            return render(request,"dashboard.html")
    return redirect('/')

def killSession(request):
    my_old_sessions = Session.objects.all()
    for row in my_old_sessions:
        return HttpResponse(row.get_decoded())
    

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
            return render(request,"dashboard.html")
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
