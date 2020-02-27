# Generated by Django 2.2.3 on 2020-02-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0014_auto_20200227_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablaelectricidad',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tablamaniexplosivos',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tablasustancias',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tablatiempoprevencionista',
            name='cr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='tablatrabajosaltura',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]