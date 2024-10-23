from django.urls import path
from . import views

urlpatterns=[
    path("prueba/", views.prueba, name="prueba"),
    path("", views.index, name="index"),
    path("saludar/<str:apellido>/",views.saludar, name="saludar"),
    path("suma/<int:num1>/<int:num2>/",views.suma, name="suma"),
    path("encuesta_form/", views.encuesta_form, name="encuesta_form"),
    path("procesar_encuesta/", views.procesar_encuesta, name="procesar_encuesta"),
    path("sumar_formulario/",views.sumar_formulario, name="sumar_formulario"),
    path("productos/", views.productos, name="productos")
]