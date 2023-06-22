# Generated by Django 3.2.8 on 2023-06-14 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0078_auto_20230613_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronograma',
            name='horas',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='horas', to='users.hora', verbose_name='Hora a seleccionar'),
        ),
    ]
