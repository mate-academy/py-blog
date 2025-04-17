from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from .models import Post, Commentary


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)

    for post in posts:
        post.comment_count = Commentary.objects.filter(post=post).count()

    context = {
        "post_list": posts,  # <-- important for test
    }
    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    paginate_by = 5


class PostCreateView(generic.CreateView):
    model = Post
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
