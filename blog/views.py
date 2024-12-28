from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Commentary, Post


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects.annotate(
            num_comments=Count("comments")
        ).order_by("-created_time")
    )

    for post in posts:
        words = post.content.split()
        if len(words) > 10:
            post.content = " ".join(words[:10]) + "..."
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "post_list": page_obj.object_list
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments
        context["comments"] = comments
        context["comment_count"] = comments.count()
        return context


@login_required
def comment_create(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        text = request.POST.get("comment")
        if text:
            Commentary.objects.create(
                post=post, user=request.user, content=text
            )
    return redirect("blog:post-detail", pk=post.id)


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        user = self.request.user
        post = form.save(commit=False)
        post.owner = user
        post.save()
        # print(f"Post saved with owner: {post.owner}")
        return super().form_valid(form)
