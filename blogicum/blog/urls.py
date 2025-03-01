from django.urls import path

from blog import views


app_name = 'blog'

urlpatterns = [
    # Главная страница блога, отображение списка постов
    path('', views.index, name='index'),

    # Страница подробностей поста по его ID
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),

    # Страница постов по категории, фильтрация по slug категории
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'
    ),
]
