from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
