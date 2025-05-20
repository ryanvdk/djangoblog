from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.IndexView.as_view(), name="blog-index"),
    path("posts", views.PostsView.as_view(), name="blog-posts"),
    path("posts/<slug:slug>", views.PostView.as_view(), name="blog-post"),
    path("read-later/", views.ReadLaterView.as_view(), name="read-later")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
