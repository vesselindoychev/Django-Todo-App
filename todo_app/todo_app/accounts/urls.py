from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from todo_app.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileDetailsView, \
    EditProfileView, ChangePasswordView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('home')), name='password redirect'),
)