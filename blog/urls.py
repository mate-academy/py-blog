from django.urls import path, include

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:pk>/",
         views.PostDetailView.as_view(),
         name="post-detail"
         ),
    path("accounts/", include("django.contrib.auth.urls")),
]
