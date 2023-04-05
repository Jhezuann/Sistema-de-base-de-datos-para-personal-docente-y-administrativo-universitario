from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

#formulario para crear un docente
class FormularioDocente(forms.ModelForm):
	contraseña = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Docente
		fields = '__all__'


#formulario para crear un administrativo
class FormularioAdministrativo(forms.ModelForm):
	#para que la contraseña salga en *
	contraseña = forms.CharField(widget=forms.PasswordInput)

	#Diciendole que campos de la tablas se van a usar para registrar un usuario
	class Meta:
		model = Administrativo
		fields = '__all__'
