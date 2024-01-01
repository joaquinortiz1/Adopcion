# Generated by Django 4.2.4 on 2024-01-01 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adoptar', '0015_remove_estadosalud_estado_salud_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(default=None, max_length=50)),
                ('direccion_sede', models.CharField(default=None, max_length=50)),
                ('region_sede', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='mascota',
            name='sede',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Adoptar.sede'),
        ),
    ]