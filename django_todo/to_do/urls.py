from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("new_task/", views.new_task, name="new_task"),
    path("task_update/", views.task_update, name="task_update"),
    path("task_view/<int:pk>/", views.task_view, name="task_view"),
    path("task_delete/<int:pk>/", views.task_delete, name="task_delete")
]