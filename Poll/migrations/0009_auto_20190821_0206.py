# Generated by Django 2.2.2 on 2019-08-21 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0008_tabla_perfil_usuario_razon_social_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabla_resultados_transporte',
            name='id',
        ),
        migrations.AlterField(
            model_name='tabla_resultados_transporte',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
