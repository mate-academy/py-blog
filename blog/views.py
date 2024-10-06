from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from blog.models import Post, Commentary, User


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "commentaries": Commentary.objects.select_related(),
        "users": User.objects.all()
    }

    return render(
        request,
        "blog/index.html",
        context=context
    )
