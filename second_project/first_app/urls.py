from django.urls import path
from . import views


# Create your views here.

urlpatterns = [
    path("", views.home, name="home_page"),
    # path("about", views.about, name='about_us'),
    path('actors', views.actors, name='movies'),
]