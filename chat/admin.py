from django.contrib import admin
from .models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'sender', 'receiver', 'created_at']
    search_fields = ['sender__username', 'receiver__username']
    list_filter = ['created_at']

    class Meta:
        model = Chat


class MessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'chat', 'sender', 'timestamp', 'is_read']
    list_filter = ['is_read', 'timestamp']
    search_fields = ['sender__username', 'content']

    class Meta:
        model = Message


admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
