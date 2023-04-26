from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('todo_app.accounts.urls')),
    path('', include('todo_app.base.urls')),
]
