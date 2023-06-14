# Generated by Django 4.2.1 on 2023-06-13 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0066_remove_reservacliente_horafin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacliente',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idCliente', to=settings.AUTH_USER_MODEL),
        ),
    ]
