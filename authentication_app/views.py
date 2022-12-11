from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password,check_password

from chat_app.models import  UserAccount,Language

# Create your views here.
def auth_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = UserAccount.objects.filter(username=username).first()
        if user:
            if check_password(password,user.password):
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("incorrect password")
        else:
            return HttpResponse("no records found for username")

    return render(request,"signin.html")

def auth_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = UserAccount.objects.filter(username=username).first()
        if user:
            return HttpResponse("username not available")
        else:
            user = UserAccount(username=username,email=email,password=make_password(password))
            user.save()
            login(request,user)
            return HttpResponseRedirect("/")
            
    return render(request,"signup.html")

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def auth_reset_password(request):
    return HttpResponse("resetting password")

