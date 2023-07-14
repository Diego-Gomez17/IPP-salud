from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404


from .forms import EnfermedadForm, EtapaForm, SintomasForm, NotificacionPacienteForm
from .models import Enfermedad, Etapa, Sintomas, NotificacionPaciente

# Create your views here.
class Home(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enfermedades = Enfermedad.objects.all()
        etapas = Etapa.objects.all()
        sintomas = Sintomas.objects.all()
        notificaciones = NotificacionPaciente.objects.all()
        context['enfermedades'] = enfermedades
        context['etapas'] = etapas
        context['sintomas'] = sintomas
        context['notificaciones'] = notificaciones
        return context


class EnfermedadCreateView(CreateView):
    model = Enfermedad
    form_class = EnfermedadForm
    template_name = 'enfermedad_create.html'
    success_url = '/'

class EtapaCreateView(CreateView):
    model = Etapa
    form_class = EtapaForm
    template_name = 'etapa_create.html'
    success_url = '/'

    def form_valid(self, form):
        enfermedad = get_object_or_404(Enfermedad, id_enfermedad=self.kwargs['enfermedad_id'])
        form.instance.enfermedad = enfermedad
        return super().form_valid(form)

class SintomasCreateView(CreateView):
    model = Sintomas
    form_class = SintomasForm
    template_name = 'sintomas_create.html'
    success_url = '/'

    def form_valid(self, form):
        enfermedad = get_object_or_404(Enfermedad, id_enfermedad=self.kwargs['enfermedad_id'])
        etapa = get_object_or_404(Etapa, id_etapa=self.kwargs['etapa_id'])
        form.instance.enfermedad = enfermedad
        form.instance.etapa = etapa
        return super().form_valid(form)

class NotificacionPacienteCreateView(CreateView):
    model = NotificacionPaciente
    form_class = NotificacionPacienteForm
    template_name = 'notificacion_paciente_create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

