from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/marcador/$', consumers.MarcadorConsumer.as_asgi()),
]
