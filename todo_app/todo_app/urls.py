from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('todo_app.accounts.urls')),
    path('', include('todo_app.base.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
