from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from common.mixins import TitleMixin
from friendship.models import *
from posts.models import Comment, Post


class FeedListView(TitleMixin, TemplateView):
    template_name = 'feeds/index.html'
    title = 'Лента Новостей'

    def get_context_data(self, **kwargs):
        context = super(FeedListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            friends = Friendship.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
            context['posts'] = Post.objects.filter(user__in=friends.values_list('user1', flat=True)).order_by('-created') \
                | Post.objects.filter(user__in=friends.values_list('user2', flat=True)).order_by('-created') \
                  or Post.objects.filter(user=self.request.user).order_by('-created')
            context['friends'] =  Friendship.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        username = "ziyoviddin"  # Замените на имя пользователя, которое вы ищете
        user = User.objects.get(username=username)
        context['comments'] = Comment.objects.all().order_by('-created_at')
        context['posts_ziyoviddin'] = Post.objects.filter(user=5)
        return context


def search_users(request):
    search = request.GET.get('search')
    if search:
        users = User.objects.filter(username__icontains=search)
    else:
        users = User.objects.all()
    context ={
        'users': users,
        'title': 'Поиск пользователей'
    }
    return render(request, 'feeds/index.html', context)
