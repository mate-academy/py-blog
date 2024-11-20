from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="posts/", permanent=True)),
    path("posts/", include("blog.urls", namespace="blog")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
