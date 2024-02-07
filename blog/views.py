from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic

from .forms import CommentaryForm
from .models import Post


def index(request):
    all_posts = Post.objects.order_by("-created_time")
    page = Paginator(all_posts, 5)
    page_param = request.GET.get("page")
    page = page.get_page(page_param)

    context = {
        "page_obj": page,
        "is_paginated": page.has_other_pages(),
    }

    return render(request, "blog/index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)

        else:
            context = self.get_context_data(**kwargs)
            context["comment_form"] = form
            return self.render_to_response(context)
