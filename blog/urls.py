from django.urls import path

from blog.views import PostListView, PostDetailView,create_commentary_view

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create/",
        create_commentary_view,
        name="commentary-create"
    ),
]

app_name = "blog"
