from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("greeting", views.greeting, name='greeting'),
    path("intro", views.intro, name='introduction'),
    path("date", views.date, name='datetime'),
    path("task", views.task, name="dictioanry_task")

]