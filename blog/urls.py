from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import PostList, post_detail_view

urlpatterns = [
    path("post/", PostList.as_view(), name="index"),
    path("post/<int:pk>/", post_detail_view, name="post-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "blog"
