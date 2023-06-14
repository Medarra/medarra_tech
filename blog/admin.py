"""
Admin Processes for Medarra Tech Blog
"""

from django.contrib import admin
from . import models
from .models import Comment


class CommentInline(admin.StackedInline):
    model = Comment
    readonly_fields = (
        'name',
        'email',
        'text',
    )
    extra = 0


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post',
                    'name',
                    'text',
                    'created',
                    'updated',
                    )

    list_filter = (
        'approved',
    )

    search_fields = (
        'post__title',
        'name',
        'text',
        )


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

    list_display = (
        'title',
        'author',
        'created',
        'updated',
    )

    list_filter = (
        'status',
        'topics',
    )

    prepopulated_fields = {'slug': ('title',)}

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {'slug': ('name',)}
