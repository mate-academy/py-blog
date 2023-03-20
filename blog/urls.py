from django.urls import path
from blog.views import index, post_detail_retrieve_view, commentary_create_view

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", post_detail_retrieve_view, name="post-detail"),
    path(
        "post/<int:pk>/commentary/create/",
        commentary_create_view,
        name="commentary-create",
    ),
]
app_name = "blog"
