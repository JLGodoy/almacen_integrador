from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('killSession', views.killSession, name = 'killSession'),
    path('change_password', views.change_password, name='password'),
]
