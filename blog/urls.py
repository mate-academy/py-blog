from django.urls import path, include
from blog.views import index, PostDetailView


urlpatterns = [

    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]

app_name = "blog"
