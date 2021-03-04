from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    # path('newtask/', views.newtask, name='NewTask'),
    path('newtask/', views.TaskCreateView.as_view(), name='NewTask'),
    # path('taskupdate/<str:pk>/', views.taskupdate, name='TaskUpdate'),
    path('taskupdate/<str:pk>', views.TaskUpdateView.as_view(), name='TaskUpdate'),
    # path('taskview/<int:pk>/', views.taskview, name='TaskView'),
    path('taskview/<int:pk>/', views.TaskView.as_view(), name='TaskView'),
    path('taskdelete/<int:pk>/', views.taskdelete, name='TaskDelete'),
    path('all_tasks/', views.all_tasks, name='all_tasks')
]