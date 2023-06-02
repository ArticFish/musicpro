# Generated by Django 4.0.4 on 2023-06-01 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable de la categoria producto')),
                ('categoria', models.CharField(max_length=50, verbose_name='categoria')),
            ],
        ),
        migrations.CreateModel(
            name='tipopro',
            fields=[
                ('idTipopro', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable del tipo producto')),
                ('tipo', models.CharField(max_length=50, verbose_name='tipo')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='ID autoincrementable del producto')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('precio', models.IntegerField(verbose_name='Precio producto')),
                ('stock', models.IntegerField(verbose_name='Stock producto')),
                ('descripcion', models.CharField(max_length=500, verbose_name='descripcion')),
                ('preciooferta', models.IntegerField(verbose_name='Precio de oferta del producto')),
                ('oferta', models.IntegerField(verbose_name='Porcentaje de oferta del producto')),
                ('marca', models.CharField(max_length=50, verbose_name='marca')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
                ('idCategoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria')),
                ('idTipopro', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.tipopro')),
            ],
        ),
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad productos')),
                ('idProducto', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
                ('idUsuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
