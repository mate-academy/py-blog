from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import PostView, PostDetailView

urlpatterns = [
    path("", PostView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
