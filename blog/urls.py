from django.urls import path
from blog.views import index, post_detail, PostCreateView


urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/<int:pk>/", PostCreateView.as_view(), name="post_create"),
]

app_name = "blog"
