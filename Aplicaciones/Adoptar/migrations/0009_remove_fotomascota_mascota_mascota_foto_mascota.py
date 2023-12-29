# Generated by Django 4.2.4 on 2023-12-29 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adoptar', '0008_alter_mascota_especie_alter_mascota_raza'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotomascota',
            name='mascota',
        ),
        migrations.AddField(
            model_name='mascota',
            name='foto_mascota',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Adoptar.fotomascota'),
        ),
    ]
