# Generated by Django 4.2 on 2023-05-24 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_rename_tservicio_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='informacion',
            field=models.TextField(default='Sin description', max_length=2000, null=True),
        ),
    ]
