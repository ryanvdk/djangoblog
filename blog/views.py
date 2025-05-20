from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CommentForm


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    # This property sets ordering, list ordering methods.
    odering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


# def index(request):
#     """
#     path: /
#     Returns the rendered index page.
#     """
#     # [:3] Python slicing syntax This line gets the 3 newest posts.
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

# def posts(request):
#     """
#     path: /posts
#     Returns the rendered posts list page.
#     """
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/posts.html", {
#         "posts": all_posts
#     })


class PostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return render(request, "blog/single-post.html", {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        })

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            # Must re-add a reference to the post on submit.
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("blog-post", args=[slug]))

        return render(request, "blog/single-post.html", {
            "post": post,
            "tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        })

# class PostView(DetailView):
#     template_name = "blog/single-post.html"
#     model = Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm()
#         return context

# def post(request, slug):
#     """
#     path: /posts/slug
#     Returns the rendered post page.
#     """
#     post_data = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/single-post.html", {
#         "post": post_data,
#         "tags": post_data.tags.all()
#     })
