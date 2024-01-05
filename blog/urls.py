from django.urls import path
from blog.views import (IndexViews,
                        PostDetailViews,
                        PostUpdateView,
                        PostDeleteView,
                        create_comment
                        )


urlpatterns = [
    path("index/", IndexViews.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailViews.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("commentary/<int:pk>/create/", create_comment, name="commentary-create"),
    ]


app_name = "blog"
