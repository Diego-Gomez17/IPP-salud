from django import forms
from .models import Enfermedad, Etapa, Sintomas, NotificacionPaciente

class EnfermedadForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = ['nombre', 'clasificacion_notificacion']
        
class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ['nombre', 'duracion']

class SintomasForm(forms.ModelForm):
    class Meta:
        model = Sintomas
        fields = ['sintoma_detalle','cuidados', 'consideraciones', 'obligatoriedad']
        widgets = {
            'obligatoriedad': forms.TextInput(attrs={'required': False}),
        }

class NotificacionPacienteForm(forms.ModelForm):
    class Meta:
        model = NotificacionPaciente
        fields = ['enfermedad', 'etapa', 'sintoma', 'nombre', 'edad', 'genero', 'region', 'comuna',
                  'fecha_notificacion', 'fecha_alta', 'correo_paciente', 'numero_paciente',
                  'direccion_paciente', 'correo_tercera_persona', 'numero_tercera_persona',
                  'direccion_tercera_persona']
        widgets = {
            'edad': forms.DateTimeInput(attrs={'type': 'date'}),
            'fecha_notificacion': forms.DateTimeInput(attrs={'type': 'date'}),
            'fecha_alta': forms.DateTimeInput(attrs={'type': 'date'})
        }