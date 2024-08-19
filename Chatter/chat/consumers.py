# chat/consumers.py
import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )

        await self.accept()

        messages = await self.get_chat_history()
        for message in messages:
            await self.send(text_data=json.dumps({
                'message': message['content'],
                'user': message['user__username'],
                'timestamp': message['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            }))
    
    @sync_to_async
    def get_chat_history(self):
        return list(Message.objects.filter(room_name=self.room_name).order_by('timestamp').values('user__username','content','timestamp'))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope['user']

        await sync_to_async(Message.objects.create)(user=user, room_name=self.room_name, content=message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "chat.message", 
                "message": message,
                "user": user.username if user.is_authenticated else 'Anonymous'
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        user = event['user']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            'user': user
        }))