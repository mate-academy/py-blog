from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5
    template_name = "blog/index.html"
    context_object_name = "post_list"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().select_related("owner")
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ["content", "post", "user"]
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:index")
