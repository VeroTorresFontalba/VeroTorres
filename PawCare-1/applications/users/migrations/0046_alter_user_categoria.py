# Generated by Django 4.2 on 2023-06-02 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0003_alter_categoria_id'),
        ('users', '0045_merge_20230601_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='categoria',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria'),
        ),
    ]
