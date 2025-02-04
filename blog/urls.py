from django.urls import path

from blog.views import index, send_commentary, PostDetailView

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/send-commentary",
         send_commentary,
         name="send-commentary")
]

app_name = "blog"
