# Generated by Django 2.2.7 on 2019-12-06 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sucursal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('IdProducto', models.AutoField(primary_key=True, serialize=False)),
                ('NombreProducto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TiposProducto',
            fields=[
                ('IdTipoProducto', models.AutoField(primary_key=True, serialize=False)),
                ('TipoProducto', models.CharField(max_length=200)),
            ],
        ),
    ]