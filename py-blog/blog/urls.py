from django.urls import path

from blog.views import index, PostDetailView, commentary_create


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/commentaries/create",
        commentary_create,
        name="commentary-create",
    ),
]

app_name = "blog"
