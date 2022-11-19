from django.shortcuts import render
from .models import Message, Chat


def index(request):
    # print(request)
    if request.method == 'POST':
        print('reveided data ' + request.POST['message'])
        myChat = Chat.objects.get(id=2)
        Message.objects.create(
            text=request.POST['message'], chat=myChat, author=request.user, receiver=request.user
        )
    chatMessages = Message.objects.filter(chat__id = 2)
    return render(request, 'chat/index.html', {'messages': chatMessages})

    #chats = Chat.objects.get()
    # print(chats)
    # print(chats.id)
