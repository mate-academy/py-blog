from django.urls import path

from blog.views import IndexListView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
]


app_name = "blog"
