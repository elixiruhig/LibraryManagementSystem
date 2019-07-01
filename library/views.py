from django.contrib.auth import login, authenticate
from django.shortcuts import render


# Create your views here.
def homeview(request):
    return render(request,'library/home.html')

def signout(request):
    return render(request, 'library/home.html')

def login(request):
    return render(request, 'library/home.html')

def register(request):
    return render(request, 'library/home.html')