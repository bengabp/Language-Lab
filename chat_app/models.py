from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserAccount(AbstractUser):
    profile_pic = models.ImageField(upload_to = "static/profiles")
    location = models.CharField(max_length=50,default="Somewhere")
    description = models.TextField()
    def _str__(self):
        return f"<UserAccount @{self.username}"

class Language(models.Model):
    name = models.CharField(max_length=20)
    fluency = models.CharField(max_length=20,choices=(
        ("BEGINNER","beginner"),
        ("INTERMEDIATE","intermediate"),
        ("FLUENT","fluent"),
        ("NATIVE","native")
    ),default="BEGINNER")

    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE)