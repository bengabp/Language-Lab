from django.urls import path

from .views import auth_login,auth_register,auth_logout

urlpatterns = [
    path('login',auth_login,name='login'),
    path('register',auth_register,name='register'),
    path('logout',auth_logout,name='logout')
]