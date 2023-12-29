from django.contrib import admin
from .models import Usuario, Mascota, Organizacion, Region, FotoMascota, CitaAdopcion, SeguimientoAdopcion, RegistroVacuna, EstadoSalud, Especie, Raza

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Especie)
admin.site.register(Raza)
admin.site.register(Organizacion)
admin.site.register(Region)
admin.site.register(FotoMascota)
admin.site.register(CitaAdopcion)
admin.site.register(SeguimientoAdopcion)
admin.site.register(RegistroVacuna)
admin.site.register(EstadoSalud)

