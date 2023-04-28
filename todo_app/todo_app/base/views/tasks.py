from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from todo_app.base.forms.tasks import CreateTaskForm, EditTaskForm, DeleteTaskForm
from todo_app.base.models import Task


class TaskListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Task
    template_name = 'base/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object_list.filter(user=self.request.user)
        context['tasks'] = self.object_list.filter(user=self.request.user).count() > 0
        return context


class TaskCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('task lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'base/task_edit.html'

    def get_success_url(self):
        return reverse_lazy('task details', kwargs={'pk': self.object.pk})


class TaskDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Task
    form_class = DeleteTaskForm
    template_name = 'base/task_delete.html'

    def get_success_url(self):
        return reverse_lazy('task lists')


class TaskDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Task
    template_name = 'base/task_details.html'
