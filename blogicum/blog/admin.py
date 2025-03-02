from django.contrib import admin

from .models import Category, Location, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')
    list_filter = ('category', 'location', 'is_published', 'author')
    ordering = ('-pub_date',)
    date_hierarchy = 'pub_date'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Location)
