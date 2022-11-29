from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers
from .common import get_chat_id_or_default


@login_required(login_url='/login/')
def index(request, id=None):
    """Logic to display a chat to the user

    Args:
        request: the request that arrives at the controller
        id (string, optional): The id of the chat that should be displayed to the user. Defaults to None.

    Returns:
        on GET: returns the HTML view
        on POST: returns the created message
    """
    if request.method == 'POST':
        myChat = Chat.objects.get(id=request.POST['chatId'])
        message = Message.objects.create(
            text=request.POST['message'],
            chat=myChat,
            author=request.user,
            receiver=request.user
        )
        serialized_obj = serializers.serialize('json', [message])
        return JsonResponse(serialized_obj[1:-1], safe=False)


    myChat = Chat.objects.get(id=get_chat_id_or_default(id))
    chatMessages = Message.objects.filter(chat__id=myChat.pk)
    return render(request, 'chat/index.html', {
        'messages': chatMessages,
        'name': myChat.name,
        'created': myChat.created_at,
        'chatId': myChat.pk,
    })
