from django.urls import path

from todo_app.base.views.generic import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)