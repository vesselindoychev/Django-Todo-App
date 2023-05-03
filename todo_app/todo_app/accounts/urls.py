from django.urls import path

from todo_app.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileDetailsView, EditProfileView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile-details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
)