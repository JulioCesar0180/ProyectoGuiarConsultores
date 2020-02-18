# Generated by Django 2.2.3 on 2020-01-13 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0003_auto_20200109_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaPoliza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tablacertificaciones',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablaconstruccion',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablaelectricidad',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablamanejoriesgos',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablamaniexplosivos',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablamanufactura',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablaservicios',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablasustancias',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablatiempoprevencionista',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablatrabajosaltura',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
        migrations.AddField(
            model_name='tablatransporte',
            name='poliza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Poll.TablaPoliza'),
        ),
    ]