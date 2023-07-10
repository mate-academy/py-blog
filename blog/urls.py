from django.urls import path

from blog.views import Index, PostDetailView, CommentaryCreateView

app_name = "blog"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/commentary-create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]
