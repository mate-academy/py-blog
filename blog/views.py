from django.shortcuts import render

from blog.models import Post


def index(request):
    context = {
        "num_posts": Post.objects.count()
    }

    return render(request, "index.html")
