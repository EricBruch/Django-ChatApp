from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.


def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse('{ "invalid": false }', safe=False)
        else:
            return JsonResponse('{ "invalid": true }', safe=False)

    return render(request, 'login/login.html', {'redirect': redirect})


def register_view(request):
    if request.method == 'POST':
        username, password, passwordRepeat, email = request.POST['username'], request.POST['password'], request.POST['passwordRepeat'], request.POST['email']
        if password != passwordRepeat:
            return JsonResponse('{ "notMatching": true }', safe=False)
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return JsonResponse('{ "successful": true }', safe=False)

    return render(request, 'register/register.html')
