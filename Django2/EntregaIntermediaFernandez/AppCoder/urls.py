from django.urls import path
from EntregaIntermediaFernandez.views import *
 
urlpatterns = [
    path("accesorios/", accesorios, name="accesorios"),
    path("alimentos/", alimentos, name="alimentos"),
    path("contacto/", contacto, name="contacto"),
    path("servicios/", servicios,name="servicios"),
    path("inicio/", inicio,name="inicio"),
    path("registrate/", formulario, name="formulario")

]