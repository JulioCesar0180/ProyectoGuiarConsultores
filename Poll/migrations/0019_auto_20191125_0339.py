# Generated by Django 2.2.7 on 2019-11-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0018_tablacertificaciones_cr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablacertificaciones',
            name='cr',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]