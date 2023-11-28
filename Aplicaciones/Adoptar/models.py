from django.db import models
from .choices import sexos
from datetime import date

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
    telefono_organizacion=models.DecimalField(max_digits=10, decimal_places=0)
    direccion=models.CharField(max_length=50)
    sitio_web=models.URLField()

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre_organizacion)
    

class Mascota(models.Model):
    nombre_mascota=models.CharField(max_length=50)
    especie=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    color=models.CharField(max_length=50)
    sexo=models.CharField(max_length=1, choices=sexos, default='H')
    edad=models.IntegerField()
    fecha_rescate=models.DateField(default=date.today)
    descripcion=models.TextField()
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, related_name='mascotas', default=None, null=True, blank=True)
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

class FotoMascota(models.Model):
    url_foto=models.URLField()
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class CitaAdopcion(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    estado_cita=models.CharField(max_length=50)
    adoptante=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class SeguimientoAdopcion(models.Model):
    fecha=models.DateField()
    estado_seguimiento=models.CharField(max_length=50)
    adoptante=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class RegistroVacuna(models.Model):
    fecha=models.DateField()
    vacuna=models.CharField(max_length=50)
    nombre_veterinario=models.CharField(max_length=50)
    fecha_proximo_control=models.DateField()
    adoptante=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)

class EstadoSalud(models.Model):
    estado_salud=models.CharField(max_length=50)
    descripcion=models.TextField()
    #imagen_mascota=models.FieldFile()
    adoptante=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota, on_delete=models.CASCADE)