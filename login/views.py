from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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
            return render(request, 'login/login.html', {'invalidCredentials': True})

    return render(request, 'login/login.html', {'redirect': redirect})


def register_view(request):
    if request.method == 'POST':
        username, password, passwordRepeat, email = request.POST[
            'username'], request.POST['password'], request.POST['passwordRepeat'], request.POST['email']
        if password != passwordRepeat:
            return render(request, 'register/register.html', {'notMatching': True})
        user = User.objects.create_user(
            username, email, password)
        login(request, user)
        return HttpResponseRedirect('/chat/')

    return render(request, 'register/register.html')
