from datetime import timedelta

from django.db import models
from django.utils.timezone import now

from users.models import User

# from posts.models import Comment



class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='posts_images', null=True, blank=True)
    video = models.FileField(upload_to='posts_videos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', through='LikePost')

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post}'
    
    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

        Notification.objects.create(
            user=self.post.user,  
            post=self.post,      
            sender=self.user,     
            is_like=False
        )
    

class LikePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def save(self, *args, **kwargs):
        super(LikePost, self).save(*args, **kwargs)

        Notification.objects.create(
            user=self.post.user,  # Пользователю, которому принадлежит пост
            post=self.post,       # Пост, который был лайкнут
            sender=self.user,     # Пользователь, который поставил лайк
            is_like=True
        )


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications') # Пользователь, который поставил лайк или комментарий
    created_at = models.DateTimeField(auto_now_add=True)
    is_like = models.BooleanField(default=False)  # True - лайк, False - комментарий
    is_read = models.BooleanField(default=False)  # Уведомление прочитано пользователем

    def __str__(self):
        return f'Notification for {self.user.username}'
