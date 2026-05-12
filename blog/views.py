from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.annotate(
        comments_count=Count("commentaries")
    ).order_by("-created_time", "owner")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "post_list": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView, generic.edit.FormMixin):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def get_queryset(self):
        return Post.objects.annotate(comments_count=Count("commentaries"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not request.user.is_authenticated:
            return redirect(reverse("blog:post-detail", kwargs={"pk": self.object.pk}))
        content = request.POST.get("content")
        if content:
            Commentary.objects.create(
                post=self.object,
                content=content,
                user=request.user
            )
        return redirect(reverse(
            "blog:post-detail", kwargs={"pk": self.object.pk}
        ))
