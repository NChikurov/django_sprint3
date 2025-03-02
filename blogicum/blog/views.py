from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .constants import POSTS_PER_PAGE
from .models import Post, Category


def get_post_queryset():
    """Возвращает базовый QuerySet для получения постов.

    Returns:
        QuerySet: Базовый QuerySet с фильтрацией.
    """
    return (
        Post.objects.select_related('author', 'category', 'location')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        )
    )


def index(request):
    """Отображает главную страницу блога.

    Выводит последние публикованные посты.

    Args:
        request: Объект HttpRequest, представляющий запрос.

    Returns:
        HttpResponse: Объект ответа с шаблоном blog/index.html.
    """
    post_list = get_post_queryset().order_by('-pub_date')[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Отображает детальную информацию о посте.

    Выводит подробную информацию о посте с указанным ID.

    Args:
        request: Объект HttpRequest, представляющий запрос.
        post_id: Целочисленный ID запрашиваемого поста.

    Returns:
        HttpResponse: Объект ответа с шаблоном blog/detail.html.

    Raises:
        Http404: Если пост не найден или не соответствует условиям публикации.
    """
    post = get_object_or_404(get_post_queryset(), id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображает список постов в категории.

    Выводит все опубликованные посты для указанной категории.

    Args:
        request: Объект HttpRequest, представляющий запрос.
        category_slug: Строковый идентификатор категории.

    Returns:
        HttpResponse: Объект ответа с шаблоном blog/category.html.

    Raises:
        Http404: Если категория не найдена или не опубликована.
    """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = (
        get_post_queryset()
        .filter(category=category)
        .order_by('-pub_date')
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
