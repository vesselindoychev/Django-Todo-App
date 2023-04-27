from django.urls import path

from todo_app.accounts.views import LoginUserView, RegisterUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
)