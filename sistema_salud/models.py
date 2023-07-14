from django.db import models

# Create your models here.
class Enfermedad(models.Model):
    id_enfermedad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    clasificacion_notificacion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Etapa(models.Model):
    id_etapa = models.AutoField(primary_key=True)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    duracion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
class Sintomas(models.Model):
    id_sintomas = models.AutoField(primary_key=True)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    sintoma_detalle = models.TextField()
    cuidados = models.TextField()
    consideraciones = models.TextField()
    obligatoriedad = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.sintoma_detalle
    
class NotificacionPaciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    sintoma = models.ForeignKey(Sintomas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    edad = models.DateTimeField()
    genero = models.CharField(max_length=10)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    fecha_notificacion = models.DateTimeField()
    fecha_alta = models.DateTimeField()
    correo_paciente = models.CharField(max_length=30)
    numero_paciente = models.CharField(max_length=15)
    direccion_paciente = models.CharField(max_length=50)
    correo_tercera_persona = models.CharField(max_length=30)
    numero_tercera_persona = models.CharField(max_length=15)
    direccion_tercera_persona = models.CharField(max_length=50)

    def __str__(self):
        return f"Notificación Paciente #{self.id_paciente}"