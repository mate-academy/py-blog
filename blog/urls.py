from django.urls import path


from blog.views import PostDetailView, PostListView, AddCommentaryView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/add-comentary/",
        AddCommentaryView.as_view(),
        name="add-commentary"
    )
]

app_name = "blog"
