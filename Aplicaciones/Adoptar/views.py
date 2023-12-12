from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, CitaAdopcion, FotoMascota, Organizacion, Postulacion
from django.views import View
from django.contrib.auth.hashers import make_password
from .forms import FiltroMascotasForm, CitaForm, RegistroForm, AuthenticationForm, OrganizacionForm, OrganizacionLoginForm, PostulacionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

def lobby_organizacion(request):
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

    return render(request, 'lobby_org.html', {'mascotas': mascotas, 'form': form})
    
#def agendar_cita(request, mascota_id):
    #mascota = get_object_or_404(Mascota, pk=mascota_id)

    #if request.method == 'POST':
        #form = CitaForm(request.POST)
        #if form.is_valid():
            #fecha = form.cleaned_data['fecha']
            #hora = form.cleaned_data['hora']

            # Guarda la cita en la base de datos
            #cita = CitaAdopcion.objects.create(mascota=mascota, fecha=fecha, hora=hora)
            
            # Puedes redirigir a otra página o realizar alguna otra acción
            #return redirect('lobby')  # Cambia 'nombre_de_la_vista' por la vista deseada

    #else:
        #form = CitaForm()

    #return render(request, 'agendar_cita.html', {'mascota': mascota, 'form': form})


def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Iniciar sesión
                login(request, user)

                # Redirigir al lobby (ajusta la URL según tu configuración)
                return redirect('lobby')

    else:
        form = AuthenticationForm()

    return render(request, 'inicio_sesion.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Crea el usuario
            user = User.objects.create_user(username=username, email=email, password=password)

            # Inicia sesión automáticamente después del registro
            login(request, user)

            # Redirige al lobby (ajusta la URL según tu configuración)
            return redirect('inicio_sesion')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def inicio_sesion_organizacion(request):
    if request.method == 'POST':
        form = OrganizacionLoginForm(request.POST)
        if form.is_valid():
            nombre_organizacion = form.cleaned_data['nombre_organizacion']
            password_org = form.cleaned_data['password_org']

            # Autenticar a la organización
            organizacion = authenticate(request, nombre_organizacion=nombre_organizacion, password_org=password_org)

            if organizacion is not None:
                # Iniciar sesión
                login(request, organizacion)

                # Redirigir a donde desees después de iniciar sesión
                return redirect('lobby_organizacion')  # Ajusta la URL según tu configuración
            else:
                # Organización no encontrada o contraseña incorrecta
                messages.error(request, 'Nombre de organización o contraseña incorrectos. Inténtalo de nuevo.')

    else:
        form = OrganizacionLoginForm()

    return render(request, 'inicio_sesion_org.html', {'form': form})

def registro_organizacion(request):
    if request.method == 'POST':
        form = OrganizacionForm(request.POST)
        if form.is_valid():
            # Guarda la organización en la base de datos
            nueva_organizacion = form.save()

            # Puedes realizar otras operaciones aquí si es necesario

            # Redirige a donde desees después de registrar la organización
            return redirect('inicio_sesion_organizacion')  # Ajusta la URL según tus necesidades
    else:
        form = OrganizacionForm()

    return render(request, 'registro_org.html', {'form': form})

def mostrar_galeria(request, mascota_id):
    # Obtener la mascota seleccionada o devolver un error 404 si no existe
    mascota = get_object_or_404(Mascota, id=mascota_id)

    # Obtener todas las fotos asociadas a la mascota seleccionada
    fotos_mascota = FotoMascota.objects.filter(mascota=mascota)

    # Puedes realizar cualquier lógica adicional aquí según tus necesidades

    # Renderizar la plantilla de galería con las fotos de la mascota seleccionada
    return render(request, 'galeria.html', {'mascota': mascota, 'fotos_mascota': fotos_mascota})

def registrar_mascota(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre_mascota = request.POST['nombre_mascota']
        especie = request.POST['especie']
        raza = request.POST['raza']
        color = request.POST['color']
        sexo = request.POST['sexo']
        edad = request.POST['edad']
        fecha_rescate = request.POST['fecha_rescate']
        descripcion = request.POST['descripcion']

        # Crea una nueva mascota
        nueva_mascota = Mascota.objects.create(
            nombre_mascota=nombre_mascota,
            especie=especie,
            raza=raza,
            color=color,
            sexo=sexo,
            edad=edad,
            fecha_rescate=fecha_rescate,
            descripcion=descripcion
        )

        # Redirige a donde desees después de crear la mascota
        return redirect('lobby')
    else:
        # Si el método no es POST, renderiza el formulario
        return render(request, 'registrar_mascota.html')

def vista_organizacion(request):
    organizaciones = Organizacion.objects.all()
    print(organizaciones)  # Verifica si esta línea imprime en la consola
    return render(request, 'registrar_mascota.html', {'organizaciones': organizaciones})

def postulacion_adopcion(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
        
    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            nombre_completo = form.cleaned_data['nombre_completo']
            rut = form.cleaned_data['rut']
            estado_cita = form.cleaned_data['estado_cita']
            adoptante = form.cleaned_data['adoptante']

            # Crea la postulación
            postulacion = Postulacion.objects.create(mascota=mascota, nombre_completo=nombre_completo, rut=rut, estado_cita=estado_cita, adoptante=adoptante)
            # Lógica de postulación aquí
            # Puedes acceder a los datos del formulario usando form.cleaned_data
            return redirect('postulacion_exitosa')  # Ajusta la URL según tus necesidades
    else:
        form = PostulacionForm()

    return render(request, 'postulacion_adopcion.html', {'mascota': mascota,'form': form})

def postulacion_exitosa(request):
    return render(request, 'postulacion_exitosa.html')