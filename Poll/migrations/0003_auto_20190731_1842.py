# Generated by Django 2.2.3 on 2019-07-31 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_auto_20190731_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabla_usuario',
            name='ciudad_empresa',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='comuna_empresa',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='direccion_empresa',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='email_empresa',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='experiencia_empresa',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='nombre_contacto_empresa',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='telefono_empresa',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='tabla_usuario',
            name='ventas_anuales_empresa',
            field=models.CharField(default='', max_length=50),
        ),
    ]
