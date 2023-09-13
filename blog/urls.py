from django.urls import path
from blog.views import Index, show_post_detail, PostCreateView


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/", show_post_detail, name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create")
]

app_name = "blog"
