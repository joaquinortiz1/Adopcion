# Generated by Django 4.2.4 on 2023-12-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adoptar', '0009_remove_fotomascota_mascota_mascota_foto_mascota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto_mascota',
            field=models.ImageField(blank=True, null=True, upload_to='ruta/donde/guardar/las/fotos/'),
        ),
    ]