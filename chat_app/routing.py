from django.urls import re_path,path
from . import consumers

websocket_urlpatterns = [
    path('chat/<str:username>',consumers.ChatConsumer.as_asgi())
]