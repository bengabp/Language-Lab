from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from ..models import UserAccount,FriendRequest

class FriendsView(View):
    def get(self,request):
        context = {
            "navbar_text":"Friends",
            "friends":list(UserAccount.objects.all())*6
        }
        return render(request,"friends.html",context=context)

    def post(self,request):
        return HttpResponse("Friend request Sent")