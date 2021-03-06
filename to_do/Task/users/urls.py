from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.profile_page, name="profile_page"),
    path('update/', views.profile_update, name="profile_update"),
    path('login/', auth_views.LoginView.as_view(), name='LogIn'),
    path('logout/', auth_views.LogoutView.as_view(), name='LogOut'),
    path('create/', views.create, name='CreateUser'),
]