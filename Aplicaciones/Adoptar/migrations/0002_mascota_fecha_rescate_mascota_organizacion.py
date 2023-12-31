# Generated by Django 4.2.4 on 2023-11-22 22:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adoptar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='fecha_rescate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='mascota',
            name='organizacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mascotas', to='Adoptar.organizacion'),
        ),
    ]
