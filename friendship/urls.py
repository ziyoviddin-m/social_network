from django.urls import path

from friendship import views
from friendship.views import *

app_name = 'friendship'

urlpatterns = [
    path('send_friend/<int:to_user_id>/', views.send_friend_request, name='send_friend'),
    path('accept_friend/', views.accept_friend_request, name='accept_friend'),
    path('other_user/<int:user_id>/', views.profile_other_user, name='other_user'),
    path('other_user_about/<int:user_id>/', views.other_user_about, name='other_user_about'),
    path('other_user_photos/<int:user_id>/', views.other_user_photos, name='other_user_photos'),
    path('other_friends/<int:user_id>/', views.other_user_friends, name='other_friends'),
    path('delete_friends/<int:user_id>/', views.delete_friends, name='delete_friends'),
]