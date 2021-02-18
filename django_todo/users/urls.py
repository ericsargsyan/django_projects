from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='login'),
    path('create_user/', views.create_user, name='create_user'),
    path('login/', views.login, name='login'),
]
