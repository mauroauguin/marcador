from django.db import models

# Create your models here.

class Marcador(models.Model):
    # Cambiar el ID a un IntegerField para un solo marcador
    id = models.IntegerField(primary_key=True, default=1)  # Usar un ID fijo
    campeonato = models.CharField(max_length=200)
    jugador1 = models.CharField(max_length=200, default="Jugador 1")
    jugador2 = models.CharField(max_length=200, default="Jugador 2")
    set1_jugador1 = models.IntegerField(default=0)
    set2_jugador1 = models.IntegerField(default=0)
    set3_jugador1 = models.IntegerField(default=0)
    set1_jugador2 = models.IntegerField(default=0)
    set2_jugador2 = models.IntegerField(default=0)
    set3_jugador2 = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.campeonato}: {self.jugador1} vs {self.jugador2} ({self.id})"
