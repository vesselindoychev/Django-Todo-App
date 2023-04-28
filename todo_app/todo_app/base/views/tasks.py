from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from todo_app.base.forms.tasks import CreateTaskForm
from todo_app.base.models import Task


class TaskListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Task
    template_name = 'base/task_list.html'


class TaskCreateView(views.CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('task lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDetailsView(views.DetailView):
    model = Task
    template_name = 'base/task_details.html'

