# Generated by Django 3.2 on 2024-11-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0002_auto_20241126_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloquehora',
            name='bh_dia',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.DeleteModel(
            name='Dia',
        ),
    ]