from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Административная панель Django.
    path('pages/', include('pages.urls')),  # Маршруты для приложения "pages".
    path('', include('blog.urls')),  # Маршруты для приложения "blog".
]
