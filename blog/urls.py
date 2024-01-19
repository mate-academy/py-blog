from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import PostListView, PostDetailView, add_comment


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/add-comment/", add_comment, name="add-comment"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "blog"
