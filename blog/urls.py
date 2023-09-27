from django.urls import include, path

from .views import PostDetailView, index

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
