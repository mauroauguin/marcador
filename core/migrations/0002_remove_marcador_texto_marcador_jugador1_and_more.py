# Generated by Django 5.1.1 on 2024-09-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marcador',
            name='texto',
        ),
        migrations.AddField(
            model_name='marcador',
            name='jugador1',
            field=models.CharField(default='ANTONIO LUQUE', max_length=200),
        ),
        migrations.AddField(
            model_name='marcador',
            name='jugador2',
            field=models.CharField(default='MIGUEL YANGUAS DIEZ', max_length=200),
        ),
        migrations.AddField(
            model_name='marcador',
            name='set1_jugador1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='marcador',
            name='set1_jugador2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='marcador',
            name='set2_jugador1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='marcador',
            name='set2_jugador2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='marcador',
            name='set3_jugador1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='marcador',
            name='set3_jugador2',
            field=models.IntegerField(default=0),
        ),
    ]
