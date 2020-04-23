import html

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.decorators.csrf import requires_csrf_token

from blogging.models import Post, Comment
from blogging.forms import CommentForm

def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by("-published_date")
    context = {"posts": posts}

    return render(request, "blogging/list.html", context)

@requires_csrf_token
def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.author = request.user
            instance.save()
            return redirect(request.get_full_path())
    else:
        form = CommentForm()

    comments = post.comments.all()
    context = {"post": post, "form": form, "comments": comments}
    return render(request, "blogging/detail.html", context)
