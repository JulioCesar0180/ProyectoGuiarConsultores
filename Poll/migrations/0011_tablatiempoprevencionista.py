# Generated by Django 2.2.7 on 2019-11-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0010_tablaresultadosmanejoriesgo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaTiempoPrevencionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_prevensionista', models.CharField(max_length=150)),
            ],
        ),
    ]