from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models


def home(request):
    data = {
        'greeting': 'hello'
    }

    return render(request, 'main/home.html', data)
