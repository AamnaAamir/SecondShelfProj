from django.urls import path
from .views import chat_list, chat_detail, send_message

urlpatterns = [
    path('chats/', chat_list, name='chat_list'),
    path('chats/<int:chat_id>/', chat_detail, name='chat_detail'),
    path('chats/<int:chat_id>/send/', send_message, name='send_message'),
]
