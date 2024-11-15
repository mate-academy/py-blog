from django.urls import path
from .views import IndexListView, PostDetailView, post_detail_view


urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail_view, name="post-detail")
]

app_name = "blog"
