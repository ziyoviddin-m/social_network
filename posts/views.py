from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, View

from posts.forms import CreatePostForm

from .models import LikePost, Post


@login_required
def create_post(request):
    if request.method == "POST":
        post_form = CreatePostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('feeds:home')
    else:
        post_form = CreatePostForm()
        
    context = {
        'post_form': post_form,
        'title': 'ZIYOVIDDIN - Создать пост'
    }
    return render(request, 'posts/create-post.html', context)


@login_required
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def create_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    post.comment_set.create(user=request.user, post=post, text=request.POST['comment_text'])
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    like, created = LikePost.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()      
    return HttpResponseRedirect(request.META['HTTP_REFERER'])