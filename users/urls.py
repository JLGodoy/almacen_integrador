from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.loginpage, name='loginpage'),
    path('register', views.register, name = 'register')
]
