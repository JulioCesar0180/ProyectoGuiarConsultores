# Generated by Django 2.2.7 on 2019-11-25 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0021_auto_20191125_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablaelectricidad',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablamaniexplosivos',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablasustancias',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='tablatrabajosaltura',
            name='ri',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]