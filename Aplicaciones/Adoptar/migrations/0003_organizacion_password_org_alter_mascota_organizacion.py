# Generated by Django 4.2.4 on 2023-12-11 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adoptar', '0002_mascota_fecha_rescate_mascota_organizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='password_org',
            field=models.CharField(default='default_value', max_length=50),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='organizacion',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to='Adoptar.organizacion'),
        ),
    ]
