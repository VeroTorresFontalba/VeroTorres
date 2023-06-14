# Generated by Django 4.2.1 on 2023-06-13 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0064_alter_diareserva_fechareserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservaCliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EstadoReserva', to='users.estadoreserva')),
                ('fechaReserva', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FechaReserva', to='users.diareserva')),
                ('horaFin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HoraFin', to='users.diareserva')),
                ('horaInicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HoraInicio', to='users.diareserva')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
