from django.contrib import admin

from friendship.models import *


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['user1', 'user2', 'created_at']


@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'created_at', 'accepted']


@admin.register(FriendshipRequestNotification)
class FriendshipRequestNotificationAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'friend_request', 'created_at', 'viewed']