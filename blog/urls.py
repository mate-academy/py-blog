from django.urls import path
from django.views.generic import RedirectView
from .views import index, PostDetailView

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("blog/", RedirectView.as_view(url="/blog/", permanent=False), name="redirect"),
]
