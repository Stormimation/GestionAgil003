# Generated by Django 3.1.7 on 2021-11-21 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_usuariom'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioS',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
