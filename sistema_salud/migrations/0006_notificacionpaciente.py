# Generated by Django 3.2.7 on 2023-07-14 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_salud', '0005_alter_sintomas_obligatoriedad'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionPaciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.DateTimeField()),
                ('genero', models.CharField(max_length=10)),
                ('region', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('fecha_notificacion', models.DateTimeField()),
                ('fecha_alta', models.DateTimeField()),
                ('correo_paciente', models.CharField(max_length=30)),
                ('numero_paciente', models.CharField(max_length=15)),
                ('direccion_paciente', models.CharField(max_length=50)),
                ('correo_tercera_persona', models.CharField(max_length=30)),
                ('numero_tercera_persona', models.CharField(max_length=15)),
                ('direccion_tercera_persona', models.CharField(max_length=50)),
                ('enfermedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_salud.enfermedad')),
                ('etapa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_salud.etapa')),
                ('sintoma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_salud.sintomas')),
            ],
        ),
    ]
