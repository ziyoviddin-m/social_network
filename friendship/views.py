from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from friendship.models import *
from posts.models import Comment, Post
from users.models import User


@login_required
def send_friend_request(request, to_user_id):
    from_user = request.user
    to_user = get_object_or_404(User, pk=to_user_id)

    are_friends = Friendship.objects.filter(user1=from_user, user2=to_user).exists() or Friendship.objects.filter(user1=to_user, user2=from_user).exists()

    if not are_friends:
        if not FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists() \
                and not Friendship.objects.filter(user1=from_user, user2=to_user).exists():
            friend_request = FriendRequest(from_user=from_user, to_user=to_user)
            friend_request.save()

            notification = FriendshipRequestNotification(
                to_user=to_user,
                from_user=from_user,
                friend_request=friend_request
            )
            notification.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def accept_friend_request(request):
    to_user = request.user
    friend_request = FriendRequest.objects.filter(to_user=to_user, accepted=False).first()

    if friend_request:
        friend_request.accepted = True
        friend_request.save()

        Friendship.objects.create(user1=friend_request.from_user, user2=to_user)

        FriendshipRequestNotification.objects.filter(
            to_user=to_user,
            from_user=friend_request.from_user,
            friend_request=friend_request
        ).delete()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def profile_other_user(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    other_post = Post.objects.filter(user=other_user).order_by('-created')

    context = {
        'other_user': other_user,
        'other_post': other_post,
        'comments': Comment.objects.all(),
        'title': 'Профиль'
    }
    return render(request, 'friendship/profile_other_user.html', context)


def other_user_about(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    return render(request, 'friendship/about.html', {'other_user': other_user, 'title': 'Обо мне'})


def other_user_photos(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    other_post = Post.objects.filter(user=other_user).order_by('-created')

    context = {
        'other_user': other_user,
        'other_post': other_post,
        'title': 'Фотографии'
    }
    return render(request, 'friendship/photos.html', context)


def other_user_friends(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    other_friends = Friendship.objects.filter(Q(user1=other_user) | Q(user2=other_user))

    context = {
        'other_user': other_user,
        'other_friends': other_friends,
        'title': 'Друзья'
    }
    return render(request, 'friendship/friends.html', context)


@login_required
def delete_friends(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    other_friends = Friendship.objects.filter(user1=request.user, user2=other_user) or Friendship.objects.filter(user1=other_user, user2=request.user)
    friend_request = FriendRequest.objects.filter(from_user=request.user, to_user=other_user) or FriendRequest.objects.filter(from_user=other_user, to_user=request.user)
    other_friends.delete()
    friend_request.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])