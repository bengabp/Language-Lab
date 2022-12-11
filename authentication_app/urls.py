from django.urls import path

from .views import auth_login,auth_register,auth_logout,auth_reset_password

urlpatterns = [
    path('login',auth_login,name='login'),
    path('register',auth_register,name='register'),
    path('logout',auth_logout,name='logout'),
    path("reset-password",auth_reset_password,name="reset_password")
]