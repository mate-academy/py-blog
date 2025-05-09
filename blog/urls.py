from django.urls import path
from blog.views import index, PostDetailView, post_detail

app_name = 'blog'



urlpatterns = [
    path("", index, name="index"),
 #   path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/", post_detail, name="post-detail"),
]