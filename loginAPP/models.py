from django.db import models
from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

#Creando la tabla de docentes
class Docente(models.Model):
	nacionalidad = models.CharField(max_length=50)
	cedula = models.IntegerField(max_length=8, primary_key=True, unique=True)
	contraseña = models.CharField(max_length=25)
	fecha_De_Nacimiento = models.CharField(max_length=30)
	primer_Nombre = models.CharField(max_length=25)
	segundo_Nombre = models.CharField(max_length=25)
	primer_Apellido = models.CharField(max_length=25)
	segundo_Apellido = models.CharField(max_length=25)
	tipo_De_Trabajo = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	nucleo = models.CharField(max_length=100)
	lugar_De_Adscripcion = models.CharField(max_length=100)
	sexo = models.CharField(max_length=15)
	estado_Civil = models.CharField(max_length=20)
	direccion_Completa = models.CharField(max_length=100)
	telefono_Fijo = models.IntegerField(max_length=20)
	telefono_Cedular = models.IntegerField(max_length=20)
	correo_Electronico = models.EmailField()
	banco = models.CharField(max_length=30)
	tipo_De_Cuenta_Bancaria = models.CharField(max_length=20)
	numero_De_Cuenta_Bancaria = models.IntegerField(max_length=100)
	estatus = models.CharField(max_length=50)
	fecha_De_Ingreso = models.CharField(max_length=20)
	estudia_Actualmente = models.CharField(max_length=100)
	nivel_Academico = models.CharField(max_length=100)
	enfermedades_Cronica = models.CharField(max_length=150)
	medicamentos = models.CharField(max_length=150)
	talla_De_Pantalon = models.CharField(max_length=15)
	talla_De_Camisa = models.CharField(max_length=15)
	talla_De_Zapatos = models.CharField(max_length=15)
	condicion_Laboral = models.CharField(max_length=255)
	tiempo_De_Reposo = models.CharField(max_length=255)
	observaciones = models.CharField(max_length=255)

	#beneficiario del docente
	cedula_De_Identidad_Beneficiario = models.IntegerField(max_length=8, unique=True)
	fecha_De_Nacimiento_Beneficiario = models.CharField(max_length=30)
	primer_Nombre_Beneficiario = models.CharField(max_length=25)
	segundo_Nombre_Beneficiario = models.CharField(max_length=25)
	primer_Apellido_Beneficiario = models.CharField(max_length=25)
	segundo_Apellido_Beneficiario = models.CharField(max_length=25)
	parentezco_Beneficiario = models.CharField(max_length=50)
	sexo_Beneficiario = models.CharField(max_length=20)
	edad_Beneficiario = models.IntegerField(max_length=3)
	estado_Civil_Beneficiario = models.CharField(max_length=20)
	hijos_Beneficiario = models.CharField(max_length=30)
	estudia_Actualmente_Beneficiario = models.CharField(max_length=50)
	nivel_Academico_Beneficiario = models.CharField(max_length=150)
	enfermedades_Cronica_Beneficiario = models.CharField(max_length=255)
	medicamentos_Beneficiario = models.CharField(max_length=255)
	observaciones_Beneficiario = models.CharField(max_length=255)

	def __str__(self):
		return self.primer_Nombre + ' ' + self.primer_Apellido

	def save(self, *args, **kwargs):
		self.contraseña = make_password(self.contraseña)
		super(Docente, self).save(*args, **kwargs)

#creando la tabla administrativo
class Administrativo(models.Model):
	nacionalidad = models.CharField(max_length=50)
	cedula = models.IntegerField(max_length=8, primary_key=True, unique=True)
	contraseña = models.CharField(max_length=25)
	fecha_De_Nacimiento = models.CharField(max_length=30)
	primer_Nombre = models.CharField(max_length=25)
	segundo_Nombre = models.CharField(max_length=25)
	primer_Apellido = models.CharField(max_length=25)
	segundo_Apellido = models.CharField(max_length=25)
	tipo_De_Trabajo = models.CharField(max_length=50)
	cargo = models.CharField(max_length=100)
	nucleo = models.CharField(max_length=100)
	lugar_De_Adscripcion = models.CharField(max_length=100)
	sexo = models.CharField(max_length=15)
	estado_Civil = models.CharField(max_length=20)
	direccion_Completa = models.CharField(max_length=100)
	telefono_Fijo = models.IntegerField(max_length=20)
	telefono_Cedular = models.IntegerField(max_length=20)
	correo_Electronico = models.EmailField()
	banco = models.CharField(max_length=30)
	tipo_De_Cuenta_Bancaria = models.CharField(max_length=20)
	numero_De_Cuenta_Bancaria = models.IntegerField(max_length=100)
	estatus = models.CharField(max_length=50)
	fecha_De_Ingreso = models.CharField(max_length=20)
	estudia_Actualmente = models.CharField(max_length=100)
	nivel_Academico = models.CharField(max_length=100)
	enfermedades_Cronica = models.CharField(max_length=150)
	medicamentos = models.CharField(max_length=150)
	talla_De_Pantalon = models.CharField(max_length=15)
	talla_De_Camisa = models.CharField(max_length=15)
	talla_De_Zapatos = models.CharField(max_length=15)
	condicion_Laboral = models.CharField(max_length=255)
	tiempo_De_Reposo = models.CharField(max_length=255)
	observaciones = models.CharField(max_length=255)

	#beneficiario del docente
	cedula_De_Identidad_Beneficiario = models.IntegerField(max_length=8, unique=True)
	fecha_De_Nacimiento_Beneficiario = models.CharField(max_length=30)
	primer_Nombre_Beneficiario = models.CharField(max_length=25)
	segundo_Nombre_Beneficiario = models.CharField(max_length=25)
	primer_Apellido_Beneficiario = models.CharField(max_length=25)
	segundo_Apellido_Beneficiario = models.CharField(max_length=25)
	parentezco_Beneficiario = models.CharField(max_length=50)
	sexo_Beneficiario = models.CharField(max_length=20)
	edad_Beneficiario = models.IntegerField(max_length=3)
	estado_Civil_Beneficiario = models.CharField(max_length=20)
	hijos_Beneficiario = models.CharField(max_length=30)
	estudia_Actualmente_Beneficiario = models.CharField(max_length=50)
	nivel_Academico_Beneficiario = models.CharField(max_length=150)
	enfermedades_Cronica_Beneficiario = models.CharField(max_length=255)
	medicamentos_Beneficiario = models.CharField(max_length=255)
	observaciones_Beneficiario = models.CharField(max_length=255)

	def __str__(self):
		return self.primer_Nombre + ' ' + self.primer_Apellido

	def save(self, *args, **kwargs):
		self.contraseña = make_password(self.contraseña)
		super(Administrativo, self).save(*args, **kwargs)