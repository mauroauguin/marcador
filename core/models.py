from django.db import models
import uuid

# Create your models here.

class Marcador(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campeonato = models.CharField(max_length=200, default="World PingPong Tour")
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

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        # Verifica si el ID es un UUID válido
        try:
            uuid.UUID(str(instance.id))
        except ValueError:
            # Si no es válido, genera un nuevo UUID
            instance.id = uuid.uuid4()
        return instance

    def save(self, *args, **kwargs):
        if not self.id or not isinstance(self.id, uuid.UUID):
            self.id = uuid.uuid4()
        super().save(*args, **kwargs)
