from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import User, Post, Commentary


# @login_required
def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    is_paginated = True
    context = {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
        "is_paginated": is_paginated,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        target_post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = target_post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )
