from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog_system import settings

urlpatterns = ([
    path("admin/", admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
))
