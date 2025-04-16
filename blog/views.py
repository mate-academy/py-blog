from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    ordering = "-created_time"
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentary")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/commentary_form.html"
