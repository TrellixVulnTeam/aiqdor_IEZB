# Generated by Django 2.2.2 on 2019-06-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0004_auto_20190622_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='preco',
        ),
        migrations.AddField(
            model_name='consulta',
            name='precoC',
            field=models.FloatField(null=True),
        ),
    ]
