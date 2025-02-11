from django.urls import path

from blog.views import PostDetailView, CommentaryCreateView, index

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/commentary/create/",
         CommentaryCreateView.as_view(), name="commentary-create")
]

app_name = "blog"
