# Generated by Django 2.2.3 on 2019-11-21 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0006_auto_20191120_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaConstruccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_construccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosConstruccion',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('construccion', models.ManyToManyField(to='Poll.TablaConstruccion')),
            ],
        ),
    ]
