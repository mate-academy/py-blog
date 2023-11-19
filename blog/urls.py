from django.urls import path

from blog.views import MainView, post_detail

urlpatterns = [
    path("", MainView.as_view(), name="index"),
    path("post/<int:pk>/", post_detail, name="post-detail"),

]

app_name = "blog"
