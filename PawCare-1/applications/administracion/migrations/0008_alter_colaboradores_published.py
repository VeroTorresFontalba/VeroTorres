# Generated by Django 4.2 on 2023-06-02 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_alter_colaboradores_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaboradores',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
    ]