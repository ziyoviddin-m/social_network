from django.db import models

from users.models import User


class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends2')
    created_at = models.DateTimeField(auto_now_add=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_requests_received')
    created_at = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)


class FriendshipRequestNotification(models.Model):
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_notifications')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_request = models.ForeignKey(FriendRequest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    viewed = models.BooleanField(default=False)