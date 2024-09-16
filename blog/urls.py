from django.urls import path
from blog.views import IndexView, PostDetailedView, AuthorCreateView, \
    CommentAddView

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailedView.as_view(), name="post-detail"),
    path("accounts/sign_up/", AuthorCreateView.as_view(), name="sign_up"),
    path(
        "post/<int:pk>/comments/add",
        CommentAddView.as_view(),
        name="comment-create"
    ),
]
