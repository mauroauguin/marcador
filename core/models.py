from django.db import models

# Create your models here.

class Marcador(models.Model):
    jugador1 = models.CharField(max_length=200, default="ANTONIO LUQUE")
    jugador2 = models.CharField(max_length=200, default="MIGUEL YANGUAS DIEZ")
    set1_jugador1 = models.IntegerField(default=0)
    set2_jugador1 = models.IntegerField(default=0)
    set3_jugador1 = models.IntegerField(default=0)
    set1_jugador2 = models.IntegerField(default=0)
    set2_jugador2 = models.IntegerField(default=0)
    set3_jugador2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.jugador1} vs {self.jugador2}"
