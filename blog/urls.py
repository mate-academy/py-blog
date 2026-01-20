from django.urls import path
from blog.views import IndexView, PostDetailView, commentary_create_view


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "commentary/<int:pk>/",
        commentary_create_view,
        name="commentary-create"
    ),

]

app_name = "blog"
