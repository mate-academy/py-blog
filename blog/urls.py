from django.urls import path, include

from blog.views import index, PostDetailView, PostAddCommentView


urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/comment", PostAddCommentView.as_view(), name="post-comment"),
]

app_name = "blog"
