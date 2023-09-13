from django.db.models import Prefetch
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.order_by("-created_time").select_related("owner")
        .prefetch_related(
            Prefetch(
                "commentaries",
                queryset=Commentary.objects.select_related("user"),
                to_attr="total_commentaries"
            )
        )
    )
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("commentaries", "commentaries__user")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commentary_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        new_commentary = Commentary(
            user=request.user,
            post=post,
            content=request.POST.get("content")
        )
        new_commentary.save()
        return redirect(reverse_lazy("blog:post-detail", args=[post.pk]))
