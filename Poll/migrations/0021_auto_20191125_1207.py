# Generated by Django 2.2.7 on 2019-11-25 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0020_auto_20191125_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablaconstruccion',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablamanufactura',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablaservicios',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablatransporte',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]