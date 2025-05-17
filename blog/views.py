from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def index(request):
    """
    path: /
    Returns the rendered index page.
    """
    # [:3] Python slicing syntax This line gets the 3 newest posts.
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    """
    path: /posts
    Returns the rendered posts list page.
    """
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": all_posts
    })


def post(request, slug):
    """
    path: /posts/slug
    Returns the rendered post page.
    """
    post_data = get_object_or_404(Post, slug=slug)
    return render(request, "blog/single-post.html", {
        "post": post_data,
        "tags": post_data.tags.all()
    })
