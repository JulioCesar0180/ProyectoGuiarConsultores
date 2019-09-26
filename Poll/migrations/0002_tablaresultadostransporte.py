# Generated by Django 2.2.2 on 2019-09-15 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Poll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TablaResultadosTransporte',
            fields=[
                ('rut_empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('answer1', models.BooleanField(default=False)),
                ('answer2', models.BooleanField(default=False)),
                ('answer3', models.BooleanField(default=False)),
                ('answer4', models.BooleanField(default=False)),
                ('answer5', models.BooleanField(default=False)),
                ('answer6', models.BooleanField(default=False)),
                ('answer7', models.BooleanField(default=False)),
                ('answer8', models.BooleanField(default=False)),
                ('answer9', models.BooleanField(default=False)),
            ],
        ),
    ]