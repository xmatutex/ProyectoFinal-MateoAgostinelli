# Generated by Django 4.1 on 2022-09-13 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appinicio', '0002_remove_usuario_usuario_usuario_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]