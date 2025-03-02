from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published и поле created_at."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
        help_text='Дата добавления категории',
    )

    class Meta:
        abstract = True
