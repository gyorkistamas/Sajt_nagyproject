from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    return render(request, 'login.html')
# Create your views here.

def login_cancelled(request):
    return redirect('/')