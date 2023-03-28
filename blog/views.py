from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from blog.models import Post
from .forms import CommentForm


@login_required
def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    context = {"post_list": posts}
    return render(request, "blog/index.html", context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect("blog:post-detail", pk=post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.commentary_set.all()
        return context
