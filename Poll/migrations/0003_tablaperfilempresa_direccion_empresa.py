# Generated by Django 2.2.7 on 2020-03-14 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0002_auto_20200314_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablaperfilempresa',
            name='direccion_empresa',
            field=models.CharField(default='', max_length=50),
        ),
    ]
