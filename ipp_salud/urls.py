"""
URL configuration for ipp_salud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_salud.views import Home , EnfermedadCreateView, EtapaCreateView, SintomasCreateView, NotificacionPacienteCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('agregar-enfermedad/', EnfermedadCreateView.as_view(), name='agregar_enfermedad'),
    path('agregar-etapa/<int:enfermedad_id>/', EtapaCreateView.as_view(), name='agregar_etapa'),
    path('agregar-sintoma/<int:enfermedad_id>/<int:etapa_id>/', SintomasCreateView.as_view(), name='agregar_sintoma'),
    path('agregar-paciente/', NotificacionPacienteCreateView.as_view(), name='agregar_paciente'),


]
