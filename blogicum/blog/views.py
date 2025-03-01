from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def index(request):
    """
    Отображает главную страницу с пятью последними публикациями.
    Публикации фильтруются по дате и статусу публикации поста и категории.
    """
    post_list = Post.objects.select_related('category', 'location').filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Отображает подробности одного поста по его id."""
    post = get_object_or_404(
        Post,
        id=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """
    Отображает страницу с постами, отфильтрованными по категории.
    Выводятся только опубликованные посты с датой публикации
    не позже текущего времени.
    """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.select_related('category', 'location').filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
