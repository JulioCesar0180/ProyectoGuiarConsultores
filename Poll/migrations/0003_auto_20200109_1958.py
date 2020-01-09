# Generated by Django 2.2.7 on 2020-01-09 22:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_tablacertificaciones_tablaconstruccion_tablaelectricidad_tablamanejoriesgos_tablamaniexplosivos_tabl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaperfilempresa',
            name='experiencia_empresa',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)]),
        ),
    ]
