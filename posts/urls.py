from django.urls import path

from posts import views
from posts.views import *

app_name = 'posts'

urlpatterns = [
    path('', views.create_post, name='create-post'),
    path('delete/<int:pk>/', views.post_delete, name='delete-post'),
    path('feeds/<int:post_id>/', views.create_comment, name='create_comment'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]