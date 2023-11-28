from django.urls import path
from . import views
#from .views import AgendarCitaView

urlpatterns = [
    path('', views.index, name='index'),
    path('lobby/', views.lobby, name='lobby'),
    path('agendar_cita/<int:mascota_id>/', views.agendar_cita, name='agendar_cita'),
    path('login/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/', views.registro, name='registro'),
    path('login_organizacion/', views.inicio_sesion_organizacion, name='inicio_sesion_organizacion'),
    path('registro_organizacion/', views.registro_organizacion, name='registro_organizacion'),
    path('galeria/<int:mascota_id>/', views.mostrar_galeria, name='galeria'),
]
