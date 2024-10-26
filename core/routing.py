from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/marcador/(?P<marcador_id>[^/]+)/$', consumers.MarcadorConsumer.as_asgi()),
]
