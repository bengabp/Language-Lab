from django.urls import path

from .views import home,dashboard,tasks

urlpatterns = [
    path('',home,name='home'),
    path('dashboard',dashboard,name='dashboard'),
    path('tasks',tasks,name="tasks")
]