from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def auth_login(request):
    print(request.POST)
    return HttpResponse("Login")

def auth_register(request):
    print(request.POST)
    return HttpResponse("Register")

def auth_logout(request):
    print(request.POST)
    return HttpResponse("Logout")

