from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Organizacion, Mascota, Raza, Especie, SeguimientoAdopcion, Colecta, SeguimientoEstadoSalud
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User

class FiltroMascotasForm(forms.Form):
    especie = forms.ModelChoiceField(queryset=Especie.objects.all(), empty_label="Seleccione", required=False)
    raza = forms.ModelChoiceField(queryset=Raza.objects.all(), empty_label="Seleccione", required=False)
    sexo = forms.ChoiceField(choices=[('', 'Seleccione'), ('M', 'Macho'), ('H', 'Hembra')], required=False)

class CitaForm(forms.Form):
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(label='Hora', widget=forms.TimeInput(attrs={'type': 'time'}))

class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class AuthenticationForm(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario', max_length=100)
    #email_organizacion = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class OrganizacionRegistroForm(forms.ModelForm):
    class Meta:
        model = Organizacion
        fields = ['nombre_organizacion', 'tipo_organizacion', 'descripcion_org', 'email_organizacion', 'password_org', 'telefono_organizacion', 'direccion', 'sitio_web']
        widgets = {'password_org': forms.PasswordInput}

class OrganizacionLoginForm(forms.Form):
    nombre_organizacion = forms.CharField(label='Nombre de Organización', max_length=50)
    password_org = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre_mascota', 'especie', 'raza', 'color', 'sexo', 'edad', 'fecha_rescate', 'descripcion', 'organizacion', 'foto_mascota']

class PostulacionForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre Completo', max_length=100)
    rut = forms.CharField(label='RUT', max_length=15)
    telefono_contacto = forms.CharField(label='Teléfono de Contacto', max_length=15)
    actividad_economica = forms.CharField(label='Actividad Económica, Oficio o Profesión', max_length=100)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')

        if fecha_nacimiento:
            # Verificar si el solicitante tiene al menos 18 años
            edad = (datetime.now().date() - fecha_nacimiento).days // 365
            if edad < 18:
                raise ValidationError('Debes ser mayor de 18 años para postularte.')

        return cleaned_data
    
class SeguimientoAdopcionForm(forms.ModelForm):
    class Meta:
        model = SeguimientoAdopcion
        fields = ['fecha', 'estado_seguimiento']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }

class ColectaForm(forms.ModelForm):
    class Meta:
        model = Colecta
        fields = ['meta', 'fecha_limite', 'descripcion','organizacion']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'}),
        }

class SeguimientoEstadoSaludForm(forms.ModelForm):
    class Meta:
        model = SeguimientoEstadoSalud
        fields = ['foto_mascota_mia', 'vacuna_mascota', 'fecha_vacuna', 'descripcion_estado_salud']
        widgets = {
            'fecha_vacuna': forms.DateInput(attrs={'type': 'date'}),
        }