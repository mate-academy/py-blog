from django.urls import path

from blog.views import (
    IndexListView,
    PostDetailView,
    create_commentary
)

app_name = "blog"

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "<int:pk>/create",
        create_commentary,
        name="commentary-create"
    )
]
