from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    }
    return render(request,"landing_page.html",context=context)


def dashboard(request):
    context = {

    }
    return render(request,"index.html",context=context)

    
