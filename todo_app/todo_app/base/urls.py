from django.urls import path

from todo_app.base.views.generic import HomeView
from todo_app.base.views.tasks import TaskListView, TaskCreateView

urlpatterns = (
    # Home
    path('', HomeView.as_view(), name='home'),

    # Tasks
    path('tasks-lists/', TaskListView.as_view(), name='task lists'),
    path('task-create/', TaskCreateView.as_view(), name='create task'),
)