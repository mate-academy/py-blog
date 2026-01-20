from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index(request):
    list_posts = Post.objects.all()

    context = {
        'list_posts': list_posts
    }

    return render(request, 'blog/index.html', context)