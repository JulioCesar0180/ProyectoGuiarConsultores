# Generated by Django 2.2.2 on 2019-08-27 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0010_auto_20190821_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabla_perfil_usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='tabla_perfil_usuario',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]