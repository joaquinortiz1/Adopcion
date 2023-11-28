from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, CitaAdopcion, FotoMascota
from django.views import View
from .forms import FiltroMascotasForm, CitaForm

def index(request):
    return render(request, 'index.html')

def lobby(request):
    mascotas = Mascota.objects.all()

    if request.method == 'GET':
        form = FiltroMascotasForm(request.GET)
        if form.is_valid():
            especie = form.cleaned_data.get('especie')
            raza = form.cleaned_data.get('raza')
            sexo = form.cleaned_data.get('sexo')

            if especie:
                mascotas = mascotas.filter(especie=especie)
            if raza:
                mascotas = mascotas.filter(raza=raza)
            if sexo:
                mascotas = mascotas.filter(sexo=sexo)

    else:
        form = FiltroMascotasForm()

    return render(request, 'lobby.html', {'mascotas': mascotas, 'form': form})

#class AgendarCitaView(View):#
    #template_name = 'agendar_cita.html'

    #def get(self, request, mascota_id):
        #mascota = Mascota.objects.get(id=mascota_id)
        #return render(request, self.template_name, {'mascota': mascota})
    
def agendar_cita(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)

    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            hora = form.cleaned_data['hora']

            # Guarda la cita en la base de datos
            cita = CitaAdopcion.objects.create(mascota=mascota, fecha=fecha, hora=hora)
            
            # Puedes redirigir a otra página o realizar alguna otra acción
            return redirect('lobby')  # Cambia 'nombre_de_la_vista' por la vista deseada

    else:
        form = CitaForm()

    return render(request, 'agendar_cita.html', {'mascota': mascota, 'form': form})

def inicio_sesion(request):
    return render(request, 'inicio_sesion.html')

def registro(request):
    return render(request, 'registro.html')

def inicio_sesion_organizacion(request):
    return render(request, 'inicio_sesion_org.html')

def registro_organizacion(request):
    return render(request, 'registro_org.html')

def mostrar_galeria(request, mascota_id):
    # Obtener la mascota seleccionada o devolver un error 404 si no existe
    mascota = get_object_or_404(Mascota, id=mascota_id)

    # Obtener todas las fotos asociadas a la mascota seleccionada
    fotos_mascota = FotoMascota.objects.filter(mascota=mascota)

    # Puedes realizar cualquier lógica adicional aquí según tus necesidades

    # Renderizar la plantilla de galería con las fotos de la mascota seleccionada
    return render(request, 'galeria.html', {'mascota': mascota, 'fotos_mascota': fotos_mascota})

