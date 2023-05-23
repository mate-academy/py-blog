from django.shortcuts import redirect
from django.views import generic
from blog.forms import CommentaryCreateForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    fields = ["content"]

    def get_context_data(self, *args, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryCreateForm()
        return context

    def post(self, request, **kwargs):
        if self.request.method == "POST":
            Commentary.objects.create(
                user_id=request.user.id,
                content=request.POST["content"],
                post_id=kwargs["pk"]
            )
        return redirect("blog:post-detail", pk=kwargs["pk"])
