from django.urls import path

from .views import home,dashboard,tasks



from .chat_views.chat_view import ChatView
from .chat_views.notifications_view import NotificationsView
from .chat_views.friends_view import FriendsView
from .chat_views.settings_view import SettingsView
from .chat_views.search_view import SearchView

app_name = "Chatapp"

urlpatterns = [
    path('',home,name='home'),
    path('dashboard',dashboard,name='dashboard'),
    path('tasks',tasks,name="tasks"),
    path('chats/<str:username>',ChatView.as_view(),name="chats"),

    path('notifications',NotificationsView.as_view(),name="notifications"),
    path('friends',FriendsView.as_view(),name="friends"),
    path("search",SearchView.as_view(),name="search"),
    path("settings",SettingsView.as_view(),name="settings")

]