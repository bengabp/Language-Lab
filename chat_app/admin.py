from django.contrib import admin
from .models import UserAccount,Language

# Register your models here.
admin.site.register(Language)
admin.site.register(UserAccount)