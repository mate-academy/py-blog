from django.urls import path

from blog.views import IndexView, PostView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostView.as_view(), name="post-detail"),
]

app_name = "blog"
