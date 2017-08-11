from django.contrib import admin
from .models import Post, Comment, Tag, Like
from django_summernote.admin import SummernoteModelAdmin


class PostModelAdmin(SummernoteModelAdmin):
     pass

admin.site.register(Post, PostModelAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_disply = ['name']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass