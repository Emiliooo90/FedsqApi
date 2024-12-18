# Generated by Django 4.2.2 on 2023-09-14 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FedsqApp', '0004_remove_plato_id_ingrediente_plato_ingredientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='id_mesa',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='clave',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rut',
        ),
        migrations.AddField(
            model_name='usuario',
            name='link',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='usuario',
            name='qrImage',
            field=models.ImageField(blank=True, upload_to='qr_folder'),
        ),
        migrations.DeleteModel(
            name='Mesa',
        ),
    ]
