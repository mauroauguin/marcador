import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Marcador

class MarcadorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.marcador_id = self.scope['url_route']['kwargs']['marcador_id']
        self.room_group_name = f'marcador_{self.marcador_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        if 'action' in text_data_json:
            if text_data_json['action'] == 'toggle_timer':
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'timer_update',
                        'action': 'toggle_timer',
                        'isRunning': text_data_json['isRunning']
                    }
                )
            elif text_data_json['action'] == 'reset_scores':
                reset_data = await self.reset_scores()
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'reset_update',
                        'action': 'reset_scores',
                        'data': reset_data
                    }
                )
            elif text_data_json['action'] in ['increase', 'decrease']:
                field = text_data_json['field']
                value = await self.update_score(field, text_data_json['action'])
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'marcador_update',
                        'field': field,
                        'value': value
                    }
                )
        elif 'field' in text_data_json and 'value' in text_data_json:
            field = text_data_json['field']
            value = text_data_json['value']
            await self.update_marcador(field, value)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'marcador_update',
                    'field': field,
                    'value': value
                }
            )

    async def marcador_update(self, event):
        field = event['field']
        value = event['value']

        await self.send(text_data=json.dumps({
            'field': field,
            'value': value
        }))

    async def timer_update(self, event):
        await self.send(text_data=json.dumps(event))

    async def reset_update(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def get_marcador(self):
        return Marcador.objects.get(id=self.marcador_id)
    
    
    @database_sync_to_async
    def update_marcador(self, field, value):
        marcador = Marcador.objects.get(id=self.marcador_id)
        setattr(marcador, field, value)
        marcador.save()

    @database_sync_to_async
    def update_score(self, field, action):
        marcador = Marcador.objects.get(id=self.marcador_id)
        current_value = getattr(marcador, field)
        
        if action == 'increase':
            new_value = current_value + 1
        elif action == 'decrease':
            new_value = max(current_value - 1, 0)  # Aseguramos que no sea negativo
        else:
            return current_value  # Si la acción no es válida, no cambiamos nada
        
        setattr(marcador, field, new_value)
        marcador.save()
        return new_value

    @database_sync_to_async
    def reset_scores(self):
        marcador = Marcador.objects.get(id=self.marcador_id)
        reset_data = {}
        for set_num in range(1, 4):
            for player in range(1, 3):
                field = f'set{set_num}_jugador{player}'
                setattr(marcador, field, 0)
                reset_data[field] = 0
        marcador.save()
        return reset_data
