from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import post_detail_view, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", post_detail_view, name="post-detail"),
]

app_name = "blog"
