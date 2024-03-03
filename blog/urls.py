from django.urls import path
from .views import index, CreateCommentView

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/",
         CreateCommentView.as_view(),
         name="comments-creates"),
]

app_name = "blog"
