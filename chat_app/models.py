from django.db import models
from django.contrib.auth.models import AbstractUser
from languagelab import settings
from .custom_exceptions import FriendRequestFailedException

# Create your models here.
class UserAccount(AbstractUser):
    profile_pic = models.ImageField(upload_to = "static/profiles")
    location = models.CharField(max_length=50,default="Somewhere")
    description = models.TextField()
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True)

    def _str__(self):
        return f"<UserAccount @{self.username}"

    


    

class FriendRequest(models.Model):
    """ Model to represent a FriendRequest """
    from_user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name="friend_request_from_user")
    to_user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,related_name="friend_request_to_user")

    @classmethod
    def send_friend_request(cls,from_user:UserAccount,to_username):
        """ Sends a friend request to a valid user object else raises an exception """
        # Check if username has an account
        to_user_account = UserAccount.objects.filter(username=to_username).first()
        if not to_user_account:
            raise FriendRequestFailedException(f"Failed while sending request. Username {to_username} is unregistered")
        
        # If username is valid, so account is valid the we proceed to send friend request
        new_friend_request = FriendRequest(from_user=from_user,to_user=to_user_account)
        new_friend_request.save()

        from_user.friend_request_to_user.add(new_friend_request)
        return new_friend_request



class Language(models.Model):
    name = models.CharField(max_length=20)
    fluency = models.CharField(max_length=20,choices=(
        ("BEGINNER","beginner"),
        ("INTERMEDIATE","intermediate"),
        ("FLUENT","fluent"),
        ("NATIVE","native")
    ),default="BEGINNER")

    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)

# class Friend(models.Model):
#     users = models.ManyToManyField(UserAccount)
#     current_user = models.ForeignKey(UserAccount,related_name="owner",null=True,on_delete=models.CASCADE)

#     @classmethod
#     def make_friend(cls,current_user,new_friend):
#         friend,created = cls.objects.get_or_create(
#             current_user = current_user
#         )