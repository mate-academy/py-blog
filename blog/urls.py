from django.urls import path
from blog.views import IndexView, PostDetailView, SendCommentView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment/", SendCommentView.as_view(),
         name="send-comment"),
]

app_name = "blog"
