# Generated by Django 4.1.7 on 2023-04-05 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('nacionalidad', models.CharField(max_length=50, null=True)),
                ('cedula', models.IntegerField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('contraseña', models.CharField(max_length=25)),
                ('fechaDeNacimiento', models.IntegerField(max_length=8, null=True)),
                ('primerNombre', models.CharField(max_length=25, null=True)),
                ('segundoNombre', models.CharField(max_length=25, null=True)),
                ('primerApellido', models.CharField(max_length=25, null=True)),
                ('segundoApellido', models.CharField(max_length=25, null=True)),
                ('tipoDeTrabajo', models.CharField(max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50, null=True)),
                ('nucleo', models.CharField(max_length=100, null=True)),
                ('lugarDeAdscripcion', models.CharField(max_length=100, null=True)),
                ('sexo', models.CharField(max_length=6, null=True)),
                ('estadoCivil', models.CharField(max_length=15, null=True)),
                ('direccionCompleta', models.CharField(max_length=100, null=True)),
                ('telefonoFijo', models.IntegerField(max_length=11, null=True)),
                ('telefonoCedular', models.IntegerField(max_length=11, null=True, unique=True)),
                ('correoElectronico', models.EmailField(max_length=254, null=True, unique=True)),
                ('banco', models.CharField(max_length=25, null=True)),
                ('tipoDeCuentaBancaria', models.CharField(max_length=15, null=True)),
                ('numeroDeCuentaBancaria', models.IntegerField(max_length=50, null=True, unique=True)),
                ('estatus', models.CharField(max_length=50, null=True)),
                ('fechaDeIngreso', models.IntegerField(max_length=8, null=True)),
                ('estudiaActualmente', models.CharField(max_length=2, null=True)),
                ('nivelAcademico', models.CharField(max_length=100, null=True)),
                ('enfermedadesCronica', models.CharField(max_length=150, null=True)),
                ('medicamentos', models.CharField(max_length=150)),
                ('tallaDePantalon', models.CharField(max_length=10, null=True)),
                ('tallaDeCamisa', models.CharField(max_length=10, null=True)),
                ('tallaDeZapatos', models.CharField(max_length=10, null=True)),
                ('condicionLaboral', models.CharField(max_length=255, null=True)),
                ('tiempoDeReposo', models.CharField(max_length=255, null=True)),
                ('observaciones', models.CharField(max_length=255, null=True)),
                ('cedulaDeIdentidadBeneficiario', models.IntegerField(max_length=8, null=True, unique=True)),
                ('fechaDeNacimientoBeneficiario', models.IntegerField(max_length=8, null=True)),
                ('primerNombreBeneficiario', models.CharField(max_length=25, null=True)),
                ('segundoNombreBeneficiario', models.CharField(max_length=25, null=True)),
                ('primerApellidoBeneficiario', models.CharField(max_length=25, null=True)),
                ('segundoApellidoBeneficiario', models.CharField(max_length=25, null=True)),
                ('parentezcoBeneficiario', models.CharField(max_length=50, null=True)),
                ('sexoBeneficiario', models.CharField(max_length=6, null=True)),
                ('edadBeneficiario', models.IntegerField(max_length=3, null=True)),
                ('estadoCivilBeneficiario', models.CharField(max_length=15, null=True)),
                ('hijosBeneficiario', models.CharField(max_length=2, null=True)),
                ('estudiaActualmenteBeneficiario', models.CharField(max_length=2, null=True)),
                ('nivelAcademicoBeneficiario', models.CharField(max_length=150, null=True)),
                ('enfermedadesCronicaBeneficiario', models.CharField(max_length=255, null=True)),
                ('medicamentosBeneficiario', models.CharField(max_length=255, null=True)),
                ('observacionesBeneficiario', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('nacionalidad', models.CharField(max_length=50, null=True)),
                ('cedula', models.IntegerField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('contraseña', models.CharField(max_length=25)),
                ('fechaDeNacimiento', models.IntegerField(max_length=8, null=True)),
                ('primerNombre', models.CharField(max_length=25, null=True)),
                ('segundoNombre', models.CharField(max_length=25, null=True)),
                ('primerApellido', models.CharField(max_length=25, null=True)),
                ('segundoApellido', models.CharField(max_length=25, null=True)),
                ('tipoDeTrabajo', models.CharField(max_length=50, null=True)),
                ('cargo', models.CharField(max_length=50, null=True)),
                ('nucleo', models.CharField(max_length=100, null=True)),
                ('lugarDeAdscripcion', models.CharField(max_length=100, null=True)),
                ('sexo', models.CharField(max_length=6, null=True)),
                ('estadoCivil', models.CharField(max_length=15, null=True)),
                ('direccionCompleta', models.CharField(max_length=100, null=True)),
                ('telefonoFijo', models.IntegerField(max_length=11, null=True)),
                ('telefonoCedular', models.IntegerField(max_length=11, null=True, unique=True)),
                ('correoElectronico', models.EmailField(max_length=254, null=True, unique=True)),
                ('banco', models.CharField(max_length=25, null=True)),
                ('tipoDeCuentaBancaria', models.CharField(max_length=15, null=True)),
                ('numeroDeCuentaBancaria', models.IntegerField(max_length=50, null=True, unique=True)),
                ('estatus', models.CharField(max_length=50, null=True)),
                ('fechaDeIngreso', models.IntegerField(max_length=8, null=True)),
                ('estudiaActualmente', models.CharField(max_length=2, null=True)),
                ('nivelAcademico', models.CharField(max_length=100, null=True)),
                ('enfermedadesCronica', models.CharField(max_length=150, null=True)),
                ('medicamentos', models.CharField(max_length=150)),
                ('tallaDePantalon', models.CharField(max_length=10, null=True)),
                ('tallaDeCamisa', models.CharField(max_length=10, null=True)),
                ('tallaDeZapatos', models.CharField(max_length=10, null=True)),
                ('condicionLaboral', models.CharField(max_length=255, null=True)),
                ('tiempoDeReposo', models.CharField(max_length=255, null=True)),
                ('observaciones', models.CharField(max_length=255, null=True)),
                ('cedulaDeIdentidadBeneficiario', models.IntegerField(max_length=8, null=True, unique=True)),
                ('fechaDeNacimientoBeneficiario', models.IntegerField(max_length=8, null=True)),
                ('primerNombreBeneficiario', models.CharField(max_length=25, null=True)),
                ('segundoNombreBeneficiario', models.CharField(max_length=25, null=True)),
                ('primerApellidoBeneficiario', models.CharField(max_length=25, null=True)),
                ('segundoApellidoBeneficiario', models.CharField(max_length=25, null=True)),
                ('parentezcoBeneficiario', models.CharField(max_length=50, null=True)),
                ('sexoBeneficiario', models.CharField(max_length=6, null=True)),
                ('edadBeneficiario', models.IntegerField(max_length=3, null=True)),
                ('estadoCivilBeneficiario', models.CharField(max_length=15, null=True)),
                ('hijosBeneficiario', models.CharField(max_length=2, null=True)),
                ('estudiaActualmenteBeneficiario', models.CharField(max_length=2, null=True)),
                ('nivelAcademicoBeneficiario', models.CharField(max_length=150, null=True)),
                ('enfermedadesCronicaBeneficiario', models.CharField(max_length=255, null=True)),
                ('medicamentosBeneficiario', models.CharField(max_length=255, null=True)),
                ('observacionesBeneficiario', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]