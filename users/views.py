from datetime import timedelta

from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from common.mixins import TitleMixin
from friendship.models import Friendship
from posts.models import Comment, Notification, Post
from users.forms import EditProfileForm, UserLoginForm, UserRegistrationForm
from users.models import User


class ProfileView(TitleMixin, ListView):
    model = User
    template_name = 'users/profile.html'
    title = 'Профиль'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user).order_by('-created')
        context['comments'] = Comment.objects.all().order_by('-created_at')
        notifications = Notification.objects.filter(user=self.request.user)
        current_time = now()
        two_days_ago = current_time - timedelta(days=3)
        old_notifications = notifications.filter(created_at__lt=two_days_ago)
        old_notifications.delete()
        context['notifications'] = notifications.order_by('-created_at')
        return context
    
    
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('feeds:home'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': 'Авторизация'
    }
    return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('feeds:home'))


class UserRegistrationView(TitleMixin, CreateView, SuccessMessageMixin):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    title = 'Регистрация'
    success_message = 'Вы успешно зарегистрировались!ы'
    
    
class EditProfileView(TitleMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'users/edit-profile.html'
    title = 'Редактирование Профиля'
    success_url = reverse_lazy('users:profile')
    


class AboutView(TitleMixin, TemplateView):
    template_name = 'users/about.html'
    title = 'Обо мне'



class PhotosView(TitleMixin, TemplateView):
    template_name = 'users/photos.html'
    title = 'Фотографии'

    def get_context_data(self, **kwargs):
        context = super(PhotosView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(user=self.request.user)
        return context


class FriendsView(TitleMixin, TemplateView):
    template_name = 'users/friends.html'    
    title = 'Друзья'

    def get_context_data(self, **kwargs):
        context = super(FriendsView, self).get_context_data(**kwargs)
        context['friends'] = Friendship.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        context['user'] = self.request.user
        return context


def delete_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    notifications.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])