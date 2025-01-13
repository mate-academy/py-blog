from django.urls import path
from blog.views import index
from blog.views import post_detail_view


urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", post_detail_view, name="post-detail"),
]

app_name = "blog"
