from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone
from django.views import generic
from django.views.generic import View

from blog.form import CommentForm
from blog.models import Post, Commentary


def index(request):
    post_list = Post.objects.filter(
        created_time__lte=timezone.now()
    ).order_by("-created_time")

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
    }

    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentary.all()
        context["comments_count"] = self.object.commentary.count()
        return context


class CommentCreateView(LoginRequiredMixin, generic.DetailView):
    @staticmethod
    def post(request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_authenticated:
            content = request.POST.get("content")
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=content
            )
        return redirect("blog:post-detail", pk=post.pk)
