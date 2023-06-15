# Generated by Django 4.2 on 2023-06-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_mascotaficha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80, unique=True, verbose_name='Tipo de mascota')),
                ('informacion', models.TextField(default='Sin description', max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'especie',
                'verbose_name_plural': 'especies',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='mascotaficha',
            name='especies',
            field=models.ManyToManyField(related_name='especies', to='users.especies', verbose_name='Tipos de mascota'),
        ),
    ]
