# Generated by Django 3.2.7 on 2023-07-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_salud', '0002_alter_enfermedad_id_enfermedad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etapa',
            name='id_etapa',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
