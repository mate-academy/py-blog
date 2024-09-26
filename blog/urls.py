from django.urls import path

from blog.views import PostListView, PostDetailView, create_commentary

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/create", create_commentary, name="commentary-create"),
]

app_name = "blog"
