from django.db import models
from django.contrib.auth.models import User

# creates db table chat_chat
class Chat(models.Model):
    # users participating in chat (2 users per chat)
    sender = models.ForeignKey(User, related_name='chat_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='chat_receiver', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat between {self.sender.username} and {self.receiver.username}"


# creates db table chat_message
class Message(models.Model):
    # each message belongs to one chat
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username}: {self.content[:20]}"
