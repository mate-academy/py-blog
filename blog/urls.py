from django.urls import path

from blog.views import Index, PostDetailView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/detail/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
