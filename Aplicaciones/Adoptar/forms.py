from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Organizacion

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