from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


@login_required(login_url='/login/')
def index(request, id=None):
    """This is a view to render the chat html.
    """
    chatId = getChatId(id)
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


def getChatId(id):
    myId = int(id) if id else 2
    return myId if myId > 2 and myId < 6 else 2
