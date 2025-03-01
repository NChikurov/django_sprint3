from django.urls import path
from django.views.generic import TemplateView

# Задаём имя пространства имен для приложения "pages"
app_name = 'pages'

urlpatterns = [
    # Маршрут для страницы "О проекте".
    path(
        'about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),

    # Маршрут для страницы "Наши правила".
    path(
        'rules/',
        TemplateView.as_view(template_name='pages/rules.html'),
        name='rules'
    ),
]
