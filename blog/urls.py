from blog.models import Commentary
from blog.views import index, PostDetailView, CommentaryCreateView

from django.urls import path

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:id>", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:id>/create",
         CommentaryCreateView.as_view(),
         name="create"),

]
