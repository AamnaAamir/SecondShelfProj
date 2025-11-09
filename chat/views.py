from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from .forms import ChatMessageForm
from django.contrib.auth.models import User

@login_required(login_url='/login')
def user_chats(request):
    chats = Chat.objects.filter(sender=request.user) | Chat.objects.filter(receiver=request.user)
    chats = chats.distinct()
    context = {
        'chats': chats
    }
    return render(request, 'chat/chats.html', context)


@login_required(login_url='/login')
def view_chat(request, chat_id):
    chat = Chat.objects.filter(id=chat_id).first()
    if chat is None or (chat.sender != request.user and chat.receiver != request.user):
        return redirect('/chat/')  # not allowed
    
    messages = Message.objects.filter(chat=chat).order_by('timestamp')
    form = ChatMessageForm(request.POST or None)
    
    if form.is_valid():
        content = form.cleaned_data.get('message')
        Message.objects.create(chat=chat, sender=request.user, content=content)
        return redirect(f'/chat/{chat.id}/')
    
    context = {
        'chat': chat,
        'messages': messages,
        'form': form
    }
    return render(request, 'chat/chat_detail.html', context)


@login_required(login_url='/login')
def start_chat(request, user_id):
    other_user = User.objects.filter(id=user_id).first()
    if other_user is None or other_user == request.user:
        return redirect('/chat/')
    
    chat, created = Chat.objects.get_or_create(
        sender=request.user,
        receiver=other_user
    )
    return redirect(f'/chat/{chat.id}/')
