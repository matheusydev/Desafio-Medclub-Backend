from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_consulta, name='criar_consulta'),
]