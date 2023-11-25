from django.urls import path
from . import views
#from .views import AgendarCitaView

urlpatterns = [
    path('lobby/', views.lobby, name='lobby'),
    path('agendar_cita/<int:mascota_id>/', views.agendar_cita, name='agendar_cita'),
    path('login/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/', views.registro, name='registro'),
]
