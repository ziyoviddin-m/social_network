from django.contrib.auth.decorators import login_required
from django.urls import path

from users import views
from users.views import *

app_name = 'users'

urlpatterns = [
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('edit-profile/<int:pk>/', login_required(EditProfileView.as_view()), name='edit-profile'),
    path('about/', login_required(AboutView.as_view()),name='about'),
    path('photos/', login_required(PhotosView.as_view()), name='photos'),
    path('friends/', login_required(FriendsView.as_view()), name='friends'),

    path('delete_notifications/', views.delete_notifications, name='delete_notifications'),
]