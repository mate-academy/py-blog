from django.urls import path
from .views import index, PostDetailView, CustomLoginView, CustomLogoutView


app_name = "blog"


urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),

    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post_detail"
    ),

    path(
        "login/",
        CustomLoginView.as_view(template_name="registration/login.html"),
        name="login"
    ),

    path(
        "logout/",
        CustomLogoutView.as_view(),
        name="logout"
    ),
]
