from django.shortcuts import render
from .models import Message, Chat


def index(request):
    # print(request)
    if request.method == 'POST':
        print('reveided data ' + request.POST['message'])
        chat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['message'], chat=chat, author=request.user, receiver=request.user)
    return render(request, 'chat/index.html', {'username': 'Eric'})
