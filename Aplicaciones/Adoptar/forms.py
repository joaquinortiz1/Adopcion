from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Organizacion, Mascota
from django.core.exceptions import ValidationError
from datetime import datetime

class FiltroMascotasForm(forms.Form):
    especie = forms.CharField(required=False)
    raza = forms.CharField(required=False)
    sexo = forms.ChoiceField(choices=[('', 'Seleccione'), ('M', 'Macho'), ('H', 'Hembra')], required=False)

class CitaForm(forms.Form):
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(label='Hora', widget=forms.TimeInput(attrs={'type': 'time'}))

class RegistroForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de Usuario', max_length=100)
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class AuthenticationForm(forms.Form):
    nombre_organizacion = forms.CharField(label='Nombre de Organizacion', max_length=100)
    #email_organizacion = forms.EmailField(label='Correo Electrónico')
    password_org = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = ['nombre_organizacion', 'email_organizacion', 'password_org']

class OrganizacionLoginForm(forms.Form):
    nombre_organizacion = forms.CharField(max_length=50)
    password_org = forms.CharField(widget=forms.PasswordInput)

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre_mascota', 'especie', 'raza', 'color', 'sexo', 'edad', 'fecha_rescate', 'descripcion']

class PostulacionForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre Completo', max_length=100)
    rut = forms.CharField(label='RUT', max_length=15)
    telefono_contacto = forms.CharField(label='Teléfono de Contacto', max_length=15)
    actividad_economica = forms.CharField(label='Actividad Económica, Oficio o Profesión', max_length=100)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento:
            # Verificar si el solicitante tiene al menos 18 años
            edad = (datetime.now().date() - fecha_nacimiento).days // 365
            if edad < 18:
                raise ValidationError('Debes ser mayor de 18 años para postularte.')
        return fecha_nacimiento