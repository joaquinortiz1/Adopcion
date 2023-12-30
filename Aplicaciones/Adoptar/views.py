from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, CitaAdopcion, FotoMascota, Organizacion, Postulacion, Raza, Especie, SeguimientoAdopcion
from django.views import View
from django.contrib.auth.hashers import make_password
from .forms import FiltroMascotasForm, CitaForm, RegistroForm, AuthenticationForm, OrganizacionRegistroForm, OrganizacionLoginForm, PostulacionForm, SeguimientoAdopcionForm, MascotaForm, ColectaForm, SeguimientoEstadoSaludForm
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
        nombre_organizacion = request.POST.get('nombre_organizacion')
        password_org = request.POST.get('password_org')

        # Autenticar a la organización
        organizacion = authenticate(request, nombre_organizacion=nombre_organizacion, password_org=password_org)

        if organizacion is not None:
            # Iniciar sesión
            login(request, organizacion)

            # Redirigir a donde desees después de iniciar sesión
            return redirect('listar_mascotas')  # Ajusta la URL según tu configuración
        else:
            # Organización no encontrada o contraseña incorrecta
            messages.error(request, 'Nombre de organización o contraseña incorrectos. Inténtalo de nuevo.')
            return redirect('lobby_organizacion')
        
    return render(request, 'inicio_sesion_org.html')



def registro_organizacion(request):
    if request.method == 'POST':
        form = OrganizacionRegistroForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            nombre_organizacion = form.cleaned_data['nombre_organizacion']
            tipo_organizacion = form.cleaned_data['tipo_organizacion']
            descripcion_org = form.cleaned_data['descripcion_org']
            email_organizacion = form.cleaned_data['email_organizacion']
            password_org = form.cleaned_data['password_org']
            telefono_organizacion = form.cleaned_data['telefono_organizacion']
            direccion = form.cleaned_data['direccion']
            sitio_web = form.cleaned_data['sitio_web']

            # Crear y guardar la organización en la base de datos
            Organizacion.objects.create(
                nombre_organizacion=nombre_organizacion,
                tipo_organizacion=tipo_organizacion,
                descripcion_org=descripcion_org,
                email_organizacion=email_organizacion,
                password_org=password_org,
                telefono_organizacion=telefono_organizacion,
                direccion=direccion,
                sitio_web=sitio_web
            )

            # Redirigir a donde desees después de registrar la organización
            return redirect('inicio_sesion_organizacion')  # Ajusta la URL según tus necesidades
    else:
        form = OrganizacionRegistroForm()

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
    especies = Especie.objects.all()
    razas = Raza.objects.all()
    organizaciones = Organizacion.objects.all()

    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre_mascota = request.POST['nombre_mascota']
        especie_id = request.POST['especie']
        raza_id = request.POST['raza']
        color = request.POST['color']
        sexo = request.POST['sexo']
        edad = request.POST['edad']
        fecha_rescate = request.POST['fecha_rescate']
        descripcion = request.POST['descripcion']
        organizacion_id = request.POST['organizacion']
        foto_mascota = request.FILES.get('fotos_mascota')

        # Obtén las instancias de Especie y Raza
        especie = Especie.objects.get(pk=especie_id)
        raza = Raza.objects.get(pk=raza_id)
        organizacion = Organizacion.objects.get(pk=organizacion_id)

        # Crea una nueva mascota
        nueva_mascota = Mascota.objects.create(
            nombre_mascota=nombre_mascota,
            especie=especie,
            raza=raza,
            color=color,
            sexo=sexo,
            edad=edad,
            fecha_rescate=fecha_rescate,
            descripcion=descripcion,
            organizacion=organizacion,
            foto_mascota=foto_mascota
        )

        # Redirige a donde desees después de crear la mascota
        return redirect('listar_mascotas')

    else:
        # Si el método no es POST, renderiza el formulario
        return render(request, 'registrar_mascota.html', {'especies': especies, 'razas': razas, 'organizaciones': organizaciones})

#def vista_organizacion(request):
    #organizaciones = Organizacion.objects.all()
    #razas = Raza.objects.all()
    #print(organizaciones)  # Verifica si esta línea imprime en la consola
    #return render(request, 'registrar_mascota.html', {'organizaciones': organizaciones,'razas': razas})

def postulacion_adopcion(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    usuario = request.user  # Asumiendo que estás utilizando el sistema de autenticación de Django

    # Verifica si el usuario ya ha postulado para esta mascota
    if Postulacion.objects.filter(usuario=usuario, mascota=mascota).exists():
        # Usuario ya postuló, puedes mostrar un mensaje o redirigir a una página informativa
        return render(request, 'yapostulado.html')

    if request.method == 'POST':
        form = PostulacionForm(request.POST)
        if form.is_valid():
            # Lógica de procesamiento del formulario
            nombre_completo = form.cleaned_data['nombre_completo']
            rut = form.cleaned_data['rut']
            telefono_contacto = form.cleaned_data['telefono_contacto']
            actividad_economica = form.cleaned_data['actividad_economica']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']

            # Crea la postulación
            postulacion = Postulacion.objects.create(
                mascota=mascota,
                usuario=usuario,
                nombre_completo=nombre_completo,
                rut=rut,
                telefono_contacto=telefono_contacto,
                actividad_economica=actividad_economica,
                fecha_nacimiento=fecha_nacimiento
            )

            return redirect('postulacion_exitosa')  # Ajusta la URL según tus necesidades
    else:
        form = PostulacionForm()

    return render(request, 'postulacion_adopcion.html', {'mascota': mascota, 'form': form})

def postulacion_exitosa(request):
    return render(request, 'postulacion_exitosa.html')

@login_required
def seguimiento_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    usuario = request.user

    # Verifica si el usuario ha postulado para esta mascota
    if not Postulacion.objects.filter(usuario=usuario, mascota=mascota).exists():
        # El usuario no ha postulado, puedes mostrar un mensaje o redirigir a una página informativa
        return render(request, 'no_adopto.html')

    # Continúa con la lógica del seguimiento
    if request.method == 'POST':
        form = SeguimientoEstadoSaludForm(request.POST)
        if form.is_valid():
            # Lógica de procesamiento del formulario de seguimiento
            # ...

            return redirect('seguimiento_exitoso')  # Ajusta la URL según tus necesidades
    else:
        form = SeguimientoEstadoSaludForm()

    return render(request, 'seguimiento_mascota.html', {'mascota': mascota, 'form': form})



def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'listar_mascotas.html', {'mascotas': mascotas})

def editar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)

    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('listar_mascotas')
    else:
        form = MascotaForm(instance=mascota)

    return render(request, 'editar_mascota.html', {'form': form, 'mascota': mascota})

def eliminar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    
    if request.method == 'POST':
        mascota.delete()
        return redirect('listar_mascotas')

    return render(request, 'eliminar_mascota.html', {'mascota': mascota})

@login_required
def crear_colecta(request):
    if request.method == 'POST':
        form = ColectaForm(request.POST)
        if form.is_valid():
            colecta = form.save(commit=False)
            colecta.organizacion = request.user.organizacion
            colecta.save()
            return redirect('index')
    else:
        form = ColectaForm()

    return render(request, 'crear_colecta.html', {'form': form})