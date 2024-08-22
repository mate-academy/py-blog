from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import (
    index,
    BlogDetailView,
    UserDetailView,
    CommentaryCreateView
)


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post-detail"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path(
        "post/<int:pk>/commentary/",
        CommentaryCreateView.as_view(),
        name="commentary_create",
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "blog"
