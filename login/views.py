from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.


def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print('asdasd', request.GET.get('next'))
            return HttpResponseRedirect(request.POST['redirect'])
        else:
            return render(request, 'login/index.html', {'invalidCredentials': True})

    return render(request, 'login/index.html', {'redirect': redirect})
