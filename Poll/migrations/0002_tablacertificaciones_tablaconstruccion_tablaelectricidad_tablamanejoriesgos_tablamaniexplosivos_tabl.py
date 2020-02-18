# Generated by Django 2.2.7 on 2019-12-20 20:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaCertificaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_certificado', models.CharField(max_length=100)),
                ('cr', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaConstruccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_construccion', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaElectricidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_elec', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaManejoRiesgos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manejo_riesgo', models.CharField(max_length=150)),
                ('cr', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaManiExplosivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_exp', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaManufactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_manufactura', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaPrioridadBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_seccion', models.CharField(max_length=50)),
                ('prioridad', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaProcesos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proceso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosDotacion',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cant_emp_contratados', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_emp_contratista', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_veh_empresa', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_veh_contratista', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_veh_empresa_pesado', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_veh_contratista_pesado', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_maq_pesada_empresa', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cant_maq_pesada_contratista', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='TablaServicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_servicios', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaSustancias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sust', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaTiempoPrevencionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_prevensionista', models.CharField(max_length=150)),
                ('cr', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaTrabajosAltura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_alt', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaTransporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_transporte', models.CharField(max_length=200)),
                ('ri', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TablaVentasAnuales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventas', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosTransporte',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('transporte', models.ManyToManyField(to='Poll.TablaTransporte')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosTiempoPreven',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('opciones_prevencionista_t', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaTiempoPrevencionista')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosSustancias',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_sust', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False)),
                ('tipos_sust', models.ManyToManyField(blank=True, null=True, to='Poll.TablaSustancias')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosServicios',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('servicios', models.ManyToManyField(to='Poll.TablaServicios')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosProcesos',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('transporte', models.BooleanField(default=False)),
                ('construccion', models.BooleanField(default=False)),
                ('manufactura', models.BooleanField(default=False)),
                ('servicios', models.BooleanField(default=False)),
                ('procesos', models.ManyToManyField(to='Poll.TablaProcesos')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosManufactura',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('manufactura', models.ManyToManyField(to='Poll.TablaManufactura')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosManiExplosivos',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_expo', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False)),
                ('tipos_exp', models.ManyToManyField(blank=True, null=True, to='Poll.TablaManiExplosivos')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosManejoRiesgo',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('opciones_manejo', models.ManyToManyField(to='Poll.TablaManejoRiesgos')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosConstruccion',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('construccion', models.ManyToManyField(to='Poll.TablaConstruccion')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosCertificaciones',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('certificaciones', models.ManyToManyField(to='Poll.TablaCertificaciones')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadosAltura',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_alt', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=False)),
                ('tipos_alt', models.ManyToManyField(blank=True, null=True, to='Poll.TablaTrabajosAltura')),
            ],
        ),
        migrations.CreateModel(
            name='TablaResultadoElectricidad',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_elec', models.BooleanField(choices=[(True, 'Sí'), (False, 'No')], default=True)),
                ('tipos_elec', models.ManyToManyField(blank=True, null=True, to='Poll.TablaElectricidad')),
            ],
        ),
        migrations.CreateModel(
            name='TablaPerfilEmpresa',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('experiencia_empresa', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('ciudad_empresa', models.CharField(default='', max_length=20)),
                ('comuna_empresa', models.CharField(default='', max_length=20)),
                ('razon_social_empresa', models.CharField(default='', max_length=100)),
                ('nombre_representante', models.CharField(default='', max_length=50)),
                ('rut_representante', models.CharField(max_length=12)),
                ('email_representante', models.EmailField(default='', max_length=50)),
                ('telefono_representante', models.CharField(default='', max_length=15)),
                ('ventas_anuales_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaVentasAnuales')),
            ],
        ),
    ]