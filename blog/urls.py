from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="blog-index"),
    path("posts", views.posts, name="blog-posts"),
    path("posts/<slug:slug>", views.post, name="blog-post")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
