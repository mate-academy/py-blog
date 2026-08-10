from django.urls import path

from blog.views import IndexListView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
