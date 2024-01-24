from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    # queryset = Post.objects.all().order_by("-created_time")
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_comments"] = Commentary.objects.count()
        return context


class PostDetailView(generic.DetailView):
    # form_class = CommentForm
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryListView(generic.ListView):
    model = Commentary


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = ("content",)
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"
