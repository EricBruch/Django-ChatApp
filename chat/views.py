from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


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
    chatId = getChatIdOrDefault(id)
    chat = Chat.objects.get(id=chatId)

    if request.method == 'POST':
        message = Message.objects.create(
            text=request.POST['message'],
            chat=chat,
            author=request.user,
            receiver=request.user
        )
        serialized_obj = serializers.serialize('json', [message])
        return JsonResponse(serialized_obj[1:-1], safe=False)

    chatMessages = Message.objects.filter(chat__id=chatId)
    return render(request, 'chat/index.html', {
        'messages': chatMessages,
        'name': chat.name,
        'created': chat.created_at
    })


def getChatIdOrDefault(id):
    myId = int(id) if id else 2
    return myId if myId > 2 and myId < 6 else 2
