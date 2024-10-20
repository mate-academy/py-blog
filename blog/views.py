from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)

    return render(request, "blog/index.html", {"post_list": post_list})


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    paginate_by = 5

    def get_object(self):
        post_id = self.kwargs.get("id")
        return get_object_or_404(Post, id=post_id)


class CommentaryCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/comment_create.html"

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, id=self.kwargs["id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", kwargs={"id": self.object.post.id}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, id=self.kwargs["id"])
        return context
