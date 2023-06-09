from django.urls import path

from todo_app.base.views.generic import HomeView
from todo_app.base.views.tasks import TaskListView, TaskCreateView, TaskDetailsView, TaskEditView, TaskDeleteView

urlpatterns = (
    # Home
    path('', HomeView.as_view(), name='home'),

    # Tasks
    path('tasks-lists/', TaskListView.as_view(), name='task lists'),
    path('task-create/', TaskCreateView.as_view(), name='create task'),
    path('task-edit/<int:pk>/', TaskEditView.as_view(), name='edit task'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='delete task'),
    path('task-details/<int:pk>/', TaskDetailsView.as_view(), name='task details'),
)