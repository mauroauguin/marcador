from django.contrib import admin
from .models import Marcador
import uuid

@admin.register(Marcador)
class MarcadorAdmin(admin.ModelAdmin):
    list_display = ('get_id', 'campeonato', 'jugador1', 'jugador2', 'created_at')
    list_filter = ('campeonato', 'created_at')
    search_fields = ('campeonato', 'jugador1', 'jugador2')
    readonly_fields = ('id', 'created_at')

    def get_id(self, obj):
        try:
            return obj.id
        except ValueError:
            return str(uuid.uuid4())  # Genera un nuevo UUID si el existente no es válido
    get_id.short_description = 'ID'

    fieldsets = (
        (None, {
            'fields': ('id', 'campeonato', 'jugador1', 'jugador2')
        }),
        ('Puntuaciones', {
            'fields': (
                ('set1_jugador1', 'set1_jugador2'),
                ('set2_jugador1', 'set2_jugador2'),
                ('set3_jugador1', 'set3_jugador2'),
            )
        }),
        ('Información adicional', {
            'fields': ('created_at',)
        }),
    )