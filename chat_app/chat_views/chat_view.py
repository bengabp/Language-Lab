from django.shortcuts import render
from django.views import View

from ..models import UserAccount


class ChatView(View):
    def get(self,request,username):

        friends = UserAccount.objects.all()

        friend_info = {
            "username":"graphene",
            "location":"Belarus/Russia",
            "profile_pic":"img/user.jpg",
            "is_active":True
        }

        user = UserAccount.objects.filter(username=username).first()
        if user:
            friend_info = user

        context = {
            "friends":friends,
            "friend_info":friend_info
        }

        return render(request,"chats.html",context=context)
    
    def post(self,request):
        pass