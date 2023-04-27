from django.urls import path

from todo_app.base.views.generic import HomeView
from todo_app.base.views.tasks import TaskListView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('tasks-lists/', TaskListView.as_view(), name='task lists'),
)