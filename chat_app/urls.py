from django.urls import path

from .views import home,dashboard,tasks,ChatView

app_name = "Chatapp"

urlpatterns = [
    path('',home,name='home'),
    path('dashboard',dashboard,name='dashboard'),
    path('tasks',tasks,name="tasks"),
    path('chats/<str:username>',ChatView.as_view(),name="chats")
]