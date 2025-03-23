from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")

    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "post_list": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context=context)
