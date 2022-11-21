from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        myChat = Chat.objects.get(id=2)
        message = Message.objects.create(
            text=request.POST['message'], chat=myChat, author=request.user, receiver=request.user
        )
        serialized_obj = serializers.serialize('json', [message])
        return JsonResponse(serialized_obj[1:-1], safe=False)
    chatMessages = Message.objects.filter(chat__id=2)
    return render(request, 'chat/index.html', {'messages': chatMessages})

    #chats = Chat.objects.get()
    # print(chats)
    # print(chats.id)
