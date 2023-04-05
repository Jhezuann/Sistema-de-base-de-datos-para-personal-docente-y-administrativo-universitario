from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

#formulario para crear un docente
class FormularioDocente(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Docente
        fields = ['cedula', 'contraseña']



"""class DocenteEditForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = [
            'nacionalidadDocente', 'contraseñaDocente', 'fechaDeNacimientoDocente','primerNombreDocente', 'segundoNombreDocente',
            'primerApellidoDocente', 'segundoApellidoDocente', 'tipoDeTrabajoDocente', 'cargoDocente', 
            'nucleoDocente', 'lugarDeAdscripcionDocente', 'sexoDocente', 'estadoCivilDocente', 'direccionCompletaDocente', 
            'telefonoFijoDocente', 'telefonoCedularDocente', 'correoElectronicoDocente', 'bancoDocente', 'tipoDeCuentaBancariaDocente', 
            'numeroDeCuentaBancariaDocente', 'estatusDocente', 'fechaDeIngresoDocente', 'estudiaActualmenteDocente', 
            'nivelAcademicoDocente', 'enfermedadesCronicaDocente', 'medicamentosDocente', 'tallaDePantalonDocente', 
            'tallaDeCamisaDocente', 'tallaDeZapatosDocente', 'condicionLaboralDocente', 'tiempoDeReposoDocente', 'observacionesDocente'
            ]"""




#formulario para crear un administrativo
class FormularioAdministrativo(forms.ModelForm):
    #para que la contraseña salga en *
    contraseña = forms.CharField(widget=forms.PasswordInput)

    #Diciendole que campos de la tablas se van a usar para registrar un usuario
    class Meta:
        model = Administrativo
        fields = ['cedula', 'contraseña']
