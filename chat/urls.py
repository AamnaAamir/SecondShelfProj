# from django.urls import path
# from .views import chat_list, chat_detail, send_message

# urlpatterns = [
#     path('chats/', chat_list, name='chat_list'),
#     path('chats/<int:chat_id>/', chat_detail, name='chat_detail'),
#     path('chats/<int:chat_id>/send/', send_message, name='send_message'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_chats, name='chat_list'),
    path('start/<int:user_id>/', views.start_chat, name='chat_start'),
    path('<int:chat_id>/', views.view_chat, name='chat_detail'),
]
