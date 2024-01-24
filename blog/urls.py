from django.conf.urls.static import static
from django.urls import path

from blog.views import PostListView, post_detail
from blog_system import settings

urlpatterns = [
    path("post/", PostListView.as_view(), name='index'),
    path("post/<int:pk>/", post_detail, name='post-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


app_name = 'blog'
