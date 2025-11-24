from django.urls.conf import path

from blog import views
from blog.views import PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comments/create/<int:pk>/",
         CommentaryCreateView.as_view(),
         name="comment-create"),
]
