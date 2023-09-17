from django.contrib import admin

from posts.models import *

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'created', 'image', 'video']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text', 'created_at']


@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'sender', 'created_at', 'is_like', 'is_read']