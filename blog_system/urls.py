from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("blog.urls", namespace="blog")),
        path("accounts/", include("django.contrib.auth.urls")),
    ]
    + debug_toolbar_urls()
)
