# Generated by Django 3.1.7 on 2021-11-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioP2',
            fields=[
                ('rut', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=300)),
                ('nombre', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
