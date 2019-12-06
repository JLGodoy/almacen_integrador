# Generated by Django 2.2.7 on 2019-12-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacenes',
            fields=[
                ('IdAlmacen', models.AutoField(primary_key=True, serialize=False)),
                ('NombreAlmacen', models.CharField(max_length=200)),
                ('Ubicacion', models.CharField(max_length=100)),
                ('IdEstatus', models.BooleanField(default=1)),
            ],
        ),
    ]