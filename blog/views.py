from django.shortcuts import render
from django.shortcuts import render


def index(request):
    """
    path: /
    Returns the rendered index page.
    """
    return render(request, "blog/index.html")


def posts(request):
    """
    path: /posts
    Returns the rendered posts list page.
    """
    pass


def post(request, slug):
    """
    path: /posts/slug
    Returns the rendered post page.
    """
    pass
