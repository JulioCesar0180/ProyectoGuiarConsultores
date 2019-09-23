# Generated by Django 2.2.3 on 2019-09-09 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Poll', '0012_merge_20190908_0251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabla_perfil_usuario',
            old_name='ventas_anuales_empresa',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='tabla_perfil_usuario',
            old_name='rut_empresa',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='ciudad_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='comuna_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='direccion_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='email_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='experiencia_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='nombre_contacto_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='nombre_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='razon_social_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='telefono_empresa',
        ),
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='user',
        ),
        migrations.AddField(
            model_name='tabla_perfil_usuario',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='tabla_perfil_usuario',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tabla_resultados_transporte',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tabla_resultados_transporte',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Tabla_perfil_empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(default='', max_length=100)),
                ('rut_empresa', models.CharField(default='', max_length=15)),
                ('direccion_empresa', models.CharField(default='', max_length=100)),
                ('experiencia_empresa', models.CharField(default='', max_length=10)),
                ('ciudad_empresa', models.CharField(default='', max_length=20)),
                ('comuna_empresa', models.CharField(default='', max_length=20)),
                ('razon_social_empresa', models.CharField(default='', max_length=100)),
                ('ventas_anuales_empresa', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tabla_perfil_usuario',
            name='empresa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Poll.Tabla_perfil_empresa'),
            preserve_default=False,
        ),
    ]