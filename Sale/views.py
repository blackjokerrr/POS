from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate

from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST.get('username'), password = request.POST.get('password'))

        if user:
            login(request, user)
            return redirect('/index/')

    return render(request, 'login/login.html')

@login_required
def index(request):
    return render(request, 'index/index.html', context = {'name': request.user.username})


def Logout(request):
    logout(request)
    return redirect('/login')

def go_login(request):
    return redirect('login/')