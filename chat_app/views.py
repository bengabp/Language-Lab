from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    context = {
    }
    return render(request,"landing_page.html",context=context)

@login_required(login_url="login")
def dashboard(request):
    context = {
        "counts":range(20)
    }
    return render(request,"index.html",context=context)


@login_required(login_url="login")
def tasks(request):
    context = {
        "counts":range(20)
    }
    return render(request,"index.html",context=context)