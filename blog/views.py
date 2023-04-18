from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data()
        context["commentary_form"] = CommentaryForm()

        return context

    def post(self, request: HttpRequest, pk: int) -> redirect:
        if self.request.method == "POST":
            Commentary.objects.create(
                user=request.user, post_id=pk, content=request.POST["content"]
            )
        return redirect("blog:post-detail", pk=pk)


def index_view(request) -> render:
    all_posts = Post.objects.all().order_by("-created_time")
    context = {"posts": all_posts}
    return render(request, "blog/post_list.html", context=context)
