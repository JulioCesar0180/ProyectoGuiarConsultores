# Generated by Django 2.2.7 on 2019-11-22 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0014_tablamaniexplosivos_tablaresultadosmaniexplosivos'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaElectricidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='tablaresultadosmaniexplosivos',
            name='is_expo',
            field=models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False),
        ),
        migrations.CreateModel(
            name='TablaResultadoElectricidad',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_elec', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False)),
                ('tipos', models.ManyToManyField(to='Poll.TablaElectricidad')),
            ],
        ),
    ]
