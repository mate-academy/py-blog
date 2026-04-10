from django.contrib import admin
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("blog.urls", "blog"), namespace="blog")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
