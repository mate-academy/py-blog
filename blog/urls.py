from django.urls import path

from blog.views import index, CommentaryListView

urlpatterns = [
    path("", index, name="index"),
    path("commentary/<int:pk>", CommentaryListView.as_view(), name="commentary")
]

app_name = "blog"
