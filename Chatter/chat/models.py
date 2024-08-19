from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chat_rooms')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_rooms')

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:20]}'