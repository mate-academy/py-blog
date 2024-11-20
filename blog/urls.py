from django.urls import path
from .views import Index, PostDetailView, PostCreateView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create")
]

app_name = "blog"
