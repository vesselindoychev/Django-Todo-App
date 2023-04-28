from django import forms

from todo_app.base.models import Task
from todo_app.common.helpers import BootstrapFormMixin


class CreateTaskForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Task
        exclude = ('user',)


class EditTaskForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_control()

    class Meta:
        model = Task
        exclude = ('user',)
