from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryCreationForm
from blog.models import Post, Commentary, User


# def index(request: HttpRequest) -> HttpResponse:
#
#     posts_per_page = 5
#
#     paginator = Paginator(Post.objects.all(), posts_per_page)
#
#     page = request.GET.get("page")
#
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     context = {
#         "posts": posts,
#     }
#
#     return render(
#         request, "blog/index.html", context=context
#     )


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.all().select_related("owner")


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            content = request.POST["content"]
            user = request.user
            post_id = kwargs["pk"]
            comment = Commentary(content=content, user=user, post_id=post_id)
            comment.save()
        return HttpResponseRedirect(
            reverse_lazy("blog:post-detail", args=[kwargs["pk"]])
        )
