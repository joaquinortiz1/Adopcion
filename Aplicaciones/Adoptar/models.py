from django.db import models
from .choices import sexos
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    telefono=models.DecimalField(max_digits=10, decimal_places=0)
    #rol_adoptante=models.CharField()
    #rol_administrador=models.CharField()

class Organizacion(models.Model):
    nombre_organizacion=models.CharField(max_length=50)
    tipo_organizacion=models.CharField(max_length=50)
    descripcion_org=models.TextField()
    email_organizacion=models.EmailField()
    password_org=models.CharField(max_length=50, default='default_value')
    telefono_organizacion=models.DecimalField(max_digits=10, decimal_places=0)
    direccion=models.CharField(max_length=50)
    sitio_web=models.URLField()


    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre_organizacion)
    
class Sede(models.Model):
   nombre_sede = models.CharField(max_length=50, default=None)
   direccion_sede = models.CharField(max_length=50, default=None)
   region_sede = models.CharField(max_length=50, default=None)

class Especie(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Raza(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class FotoMascota(models.Model):
    url_foto = models.URLField()
    imagen = models.ImageField(upload_to='fotos/', default='default.jpg')  # Cambia 'default.jpg' por el valor que desees

    def __str__(self):
        return f"Foto de {self.mascota.nombre_mascota}"

class Mascota(models.Model):
    nombre_mascota=models.CharField(max_length=50)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    color=models.CharField(max_length=50)
    sexo=models.CharField(max_length=1, choices=sexos, default='H')
    edad=models.IntegerField()
    fecha_rescate=models.DateField(default=date.today)
    descripcion=models.TextField()
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, related_name='mascotas', default=None, null=True, blank=True)
    foto_mascota = models.ImageField(upload_to='imagenes', null=True, blank=True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, default=None, null=True, blank=True)
    #foto_mascota = models.ForeignKey(FotoMascota, on_delete=models.CASCADE, null=True, blank=True, default=None)
    #adoptante=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre_mascota, self.especie, self.edad)
    
    #Crear Sede para que las organizaciones tengan diferentes sedes y que se muestre en la mascota

    
class Region(models.Model):
    nombre_region=models.CharField(max_length=50)
    nombre_comuna=models.CharField(max_length=50)
    #mascotas=models.ForeignKey(Mascota, on_delete=models.CASCADE)
    organizaciones=models.ForeignKey(Organizacion, on_delete=models.CASCADE)


class CitaAdopcion(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    estado_cita=models.CharField(max_length=50)
    adoptante=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class Postulacion(models.Model):
    nombre_completo = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    telefono_contacto = models.CharField(max_length=15)
    actividad_economica = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class SeguimientoAdopcion(models.Model):
    fecha=models.DateField()
    estado_seguimiento=models.CharField(max_length=50)
    adoptante=models.ForeignKey(User, on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class RegistroVacuna(models.Model):
    vacuna=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.vacuna)

class EstadoSalud(models.Model):
    descripcion = models.CharField(max_length=255, default='valor_predeterminado')


class Colecta(models.Model):
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)
    meta = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_limite = models.DateField()
    descripcion = models.TextField()

class SeguimientoEstadoSalud(models.Model):
    foto_mascota_mia = models.ImageField(upload_to='fotos_mascota_mia', null=True, blank=True)
    vacuna_mascota = models.ForeignKey(RegistroVacuna, on_delete=models.CASCADE)
    fecha_vacuna = models.DateField()
    descripcion_estado_salud = models.TextField()
    adoptante = models.ForeignKey(User, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)