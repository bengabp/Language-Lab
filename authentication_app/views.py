from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages

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
                messages.success(request,f"Successfully logged in as {user.username}")
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Incorrect Password")
        else:
            messages.error(request,"Sorry,the account was not found")
            messages.error(request,"This is another message")
            messages.error(request,"Lets see")

    return render(request,"signin.html")

def auth_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember = request.POST.get("remember")

        user = UserAccount.objects.filter(username=username).first()

        if user:
            messages.error(request,"Username is not available")
        else:
            user = UserAccount(username=username,email=email,password=make_password(password))
            user.save()
            login(request,user)
            messages.success(request,f"Successfully logged in as {user.username}")
            return HttpResponseRedirect("/")
            
    return render(request,"signup.html")

def auth_logout(request):
    logout(request)
    messages.success(request,"Successfully logged out")

    return HttpResponseRedirect("/")

def auth_reset_password(request):
    return HttpResponse("resetting password")

