from django.urls import path
from blog.views import PostDetailView, index

app_name = "blog"

urlpatterns = [
    # path("", IndexView.as_view(), name="index"),
    path("", index, name="index"),
    # path("posts/", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
