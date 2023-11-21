from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import PostListViews, post_detail

urlpatterns = [
    path("", PostListViews.as_view(), name="index"),
    path("post/<int:pk>/", post_detail, name="post-detail"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "blog"
