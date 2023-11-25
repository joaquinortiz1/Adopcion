from django import forms

class FiltroMascotasForm(forms.Form):
    especie = forms.CharField(required=False)
    raza = forms.CharField(required=False)
    sexo = forms.ChoiceField(choices=[('', 'Seleccione'), ('M', 'Macho'), ('H', 'Hembra')], required=False)

class CitaForm(forms.Form):
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(label='Hora', widget=forms.TimeInput(attrs={'type': 'time'}))