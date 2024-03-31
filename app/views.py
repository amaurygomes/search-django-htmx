from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'registration/login.html')

def about(request):
    return render(request, 'about.html')