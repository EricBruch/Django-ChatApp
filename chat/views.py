from django.shortcuts import render


def index(request):
    # print(request)
    if request.method == 'POST':
        print('reveided data ' + request.POST['message'])
    return render(request, 'chat/index.html', {'username': 'Eric'})
