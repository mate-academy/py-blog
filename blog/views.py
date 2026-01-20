from django.core.paginator import Paginator
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'list_posts': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'paginator': paginator,
    }

    return render(request, 'blog/index.html', context)