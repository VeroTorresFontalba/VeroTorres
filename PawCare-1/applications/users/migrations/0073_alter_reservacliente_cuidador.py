# Generated by Django 4.2.1 on 2023-06-14 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0072_reservacliente_idcuidador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservacliente',
            name='cuidador',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
