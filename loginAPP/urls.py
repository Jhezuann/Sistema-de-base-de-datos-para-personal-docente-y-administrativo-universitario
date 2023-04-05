from django.urls import path
from .views import *

#urls
urlpatterns = [
    path('inicio', inicio, name="inicio"),
    
    #Url para la cuenta admin
    path('loginAdmin/', LoginAdmin.as_view(), name='loginAdmin'), #url para el inicio de seccion del administrador
    path('homeAdmin', homeAdmin, name="homeAdmin"),

    path('crearDocente', crearDocente, name="crearDocente"),
    path('verDocente', verDocente, name="verDocente"),

    path('crearAdministrativo', CrearAdministrativo.as_view(), name="crearAdministrativo"), 
    path('verAdministrativo', verAdministrativo, name="verAdministrativo"),   

    #Url para las cuentas de los docentes
    path('loginDocente/', loginDocente, name="loginDocente"),
    path('homeDocente', homeDocente, name="homeDocente"),
    #path('editarDocente', editarDocente, name="editarDocente"),
    path('verDatos', verDatos, name="verDatos"),

    #url para las cuentas administrativas
    path('loginAdministrativo/', loginAdministrativo, name="loginAdministrativo"),
    path('homeAdministrativo', homeAdministrativo, name="homeAdministrativo"),
]