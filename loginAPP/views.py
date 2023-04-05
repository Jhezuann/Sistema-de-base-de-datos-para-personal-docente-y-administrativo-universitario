from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View
from .models import *
from .forms import *





#-------------------------iniciar seccion---------------------------
#para determinar si iniciar como admin, docente o administrativo
def inicio(request):
	return render(request, 'inicio.html')



#para entrar como admin con superuser
class LoginAdmin(LoginView):
	template_name = 'admin2/loginAdmin.html' #html que mostrara

	def get_success_url(self):
		return reverse_lazy('homeAdmin') # Redirige al usuario a la página de inicio después de iniciar sesión



#para entrar como personal docente
def loginDocente(request):
	if request.method == 'POST':
		cedula = request.POST.get('cedula')
		contraseña = request.POST.get('contraseña')
		try:
			docente = Docente.objects.get(cedula=cedula)  # Buscamos el docente por cédula.
			if check_password(contraseña, docente.contraseña):  # Comparamos contraseñas utilizando check_password().
				# Si las credenciales son correctas, redireccionamos a otra vista.
				return redirect('homeDocente')
			else:
				# Si las credenciales son incorrectas, mostramos un mensaje de error.
				error = "Cédula o contraseña incorrecta."
				return render(request, 'docentes/loginDocente.html', {'error': error})
		except Docente.DoesNotExist:
			# Si las credenciales son incorrectas, mostramos un mensaje de error.
			error = "Cédula o contraseña incorrecta."
			return render(request, 'docentes/loginDocente.html', {'error': error})
	else:
		return render(request, 'docentes/loginDocente.html')



#para entrar como personal administrativo
def loginAdministrativo(request):
	if request.method == 'POST':
		cedula = request.POST.get('cedula')
		contraseña = request.POST.get('contraseña')
		try:
			administrativo = Administrativo.objects.get(cedula=cedula)  # Buscamos el docente por cédula.
			if check_password(contraseña, administrativo.contraseña):  # Comparamos contraseñas utilizando check_password().
				# Si las credenciales son correctas, redireccionamos a otra vista.
				return redirect('homeAdministrativo')
			else:
				# Si las credenciales son incorrectas, mostramos un mensaje de error.
				error = "Cédula o contraseña incorrecta."
				return render(request, 'administrativos/loginAdministrativo.html', {'error': error})
		except Administrativo.DoesNotExist:
			# Si las credenciales son incorrectas, mostramos un mensaje de error.
			error = "Cédula o contraseña incorrecta."
			return render(request, 'administrativos/loginAdministrativo.html', {'error': error})
	else:
		return render(request, 'administrativos/loginAdministrativo.html')





#---------------------Vistas de la cuenta admin---------------------
#Inicio del admin
def homeAdmin(request):
	return render(request, 'admin2/homeAdmin.html')

#vista para crear un usuario docente
def crearDocente(request):
    if request.method == 'POST':
        form = FormularioDocente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verDocente')
    else:
        form = FormularioDocente()
    return render(request, 'admin2/registrarDocente.html', {'form': form})

#vista para ver los usuario del personal docente
def verDocente(request):
	docente=Docente.objects.all()
	return render(request, 'admin2/verDocente.html', {"docente":docente})

#Vista para crear un personal administrativo
class CrearAdministrativo(CreateView):
	model = Administrativo
	form_class = FormularioAdministrativo
	template_name = 'admin2/registrarAdministrativo.html'
	success_url = 'verAdministrativo'

#vista para ver los usuario del personal Administrativo
def verAdministrativo(request):
	administrativo=Administrativo.objects.all()
	return render(request, 'admin2/verAdministrativo.html', {"administrativo":administrativo})




#-----------------------Vistas de las cuentas del personal docente------------------
#crear una cuenta docente
#inicio del docente
def homeDocente(request):
	return render(request, 'docentes/homeDocente.html')


def verDatos(request):
	return render(request, 'docentes/verDatos.html')



#----------------------Vista de las cuentas del personal administrativo--------------
def homeAdministrativo(request):
	return render(request, 'administrativos/homeAdministrativo.html')