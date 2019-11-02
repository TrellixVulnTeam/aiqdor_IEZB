# Generated by Django 2.2.2 on 2019-06-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='endreço de email')),
                ('CPF', models.CharField(max_length=14, unique=True)),
                ('nome', models.CharField(max_length=40, verbose_name='Nome Completo')),
                ('endereco', models.CharField(max_length=40, verbose_name='Endreço')),
                ('celular', models.CharField(max_length=40)),
                ('dataNascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
