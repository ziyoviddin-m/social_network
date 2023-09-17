from django.urls import path

from feeds import views
from feeds.views import *

app_name = 'feeds'


urlpatterns = [
    path('', FeedListView.as_view(), name='home'),
    path('search_users/', views.search_users, name='search_users'),
]