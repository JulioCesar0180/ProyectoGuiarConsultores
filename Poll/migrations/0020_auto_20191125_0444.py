# Generated by Django 2.2.7 on 2019-11-25 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0019_auto_20191125_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablamanejoriesgos',
            name='cr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablatiempoprevencionista',
            name='cr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
