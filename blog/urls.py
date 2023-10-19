from django.urls import path

from blog.views import IndexView, PostDetailView, add_commentary

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/add-commentary/",
         add_commentary,
         name="commentary-create")
]

app_name = "blog"
