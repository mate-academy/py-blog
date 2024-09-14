from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request):
    posts = Post.objects.order_by("-created_time")
    paginator = Paginator(posts, 5)

    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)

    context = {
        "post_list": post_list,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            post = self.get_object()
            form = CommentaryForm(request.POST)

            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.post = post
                commentary.user = request.user
                commentary.save()
                return redirect("blog:post-detail", pk=post.pk)
        return redirect("login")
