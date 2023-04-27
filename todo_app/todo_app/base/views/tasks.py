from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from todo_app.base.models import Task


class TaskListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Task
    template_name = 'base/task_list.html'