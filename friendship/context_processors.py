from friendship.models import FriendshipRequestNotification


def notifications_friends(request):
    if request.user.is_authenticated:
        notifications = FriendshipRequestNotification.objects.filter(
            to_user=request.user,
        )
    else:
        notifications = []

    return {'notifications_friends': notifications}

