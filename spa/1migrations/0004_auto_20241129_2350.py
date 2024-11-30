# Generated by Django 3.2 on 2024-11-30 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0003_auto_20241128_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='reserva_precioTotal',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='reserva_promos',
        ),
        migrations.AlterField(
            model_name='promocion',
            name='promocion_precio',
            field=models.IntegerField(verbose_name='Descuento en CLP: '),
        ),
        migrations.RemoveField(
            model_name='promocion',
            name='promocion_servicios',
        ),
        migrations.AddField(
            model_name='promocion',
            name='promocion_servicios',
            field=models.ManyToManyField(related_name='promos', to='spa.Servicio', verbose_name='Servicios aplicables'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='reserva_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='spa.cliente'),
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='reserva_servicios',
        ),
        migrations.CreateModel(
            name='ReservaServicioPromocion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promocion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spa.promocion')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spa.reserva')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spa.servicio')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='reserva_servicios',
            field=models.ManyToManyField(related_name='reservas', through='spa.ReservaServicioPromocion', to='spa.Servicio'),
        ),
    ]
