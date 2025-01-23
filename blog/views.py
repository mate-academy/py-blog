from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic

from .models import Post
from .forms import CommentaryForm


def index(request):
    posts_list = (Post.objects.prefetch_related("comments").
                  select_related("owner").order_by("-created_time"))
    paginator = Paginator(posts_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "is_paginated": page_obj.has_other_pages(),
        "page_obj": page_obj,
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.prefetch_related("comments").
                select_related("owner"))
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        """Add comments and a form to the context."""
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        """Handle comment submission."""
        post = self.get_object()  # Get the current post
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        return self.get(request, *args, form=form, **kwargs)


# class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
#     model = Commentary
#     fields = "content"
#     success_url = reverse_lazy("blog:post-detail")
#     template_name = "blog/post_detail.html"
