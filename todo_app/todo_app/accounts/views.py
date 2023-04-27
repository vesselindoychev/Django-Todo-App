from django.contrib.auth import views as auth_views, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from todo_app.accounts.forms import CreateProfileForm
from todo_app.accounts.models import Profile


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUserView(views.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result
