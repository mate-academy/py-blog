from django.urls import path

from blog.views import (
    about,
    contact,
    RegisterView,
    PostListView,
    PostDetailView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("registration/", RegisterView.as_view(), name="register"),
]

app_name = "blog"
