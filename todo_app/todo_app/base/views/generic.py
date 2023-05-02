from django.shortcuts import redirect
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'base/home.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task lists')
        return super(HomeView, self).get(*args, **kwargs)