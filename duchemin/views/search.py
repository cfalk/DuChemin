from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models


def search(request):
    return render(request, 'search/search.html')


def query(request):
    return render()
