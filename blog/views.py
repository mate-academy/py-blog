from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary
from blog_system.forms import CommentCreationForm, PostCreationForm


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by(
        "-created_time"
    ).prefetch_related("comments")
    context_object_name = "post_list"
    paginate_by = 5


@login_required
def post_create_view(request: HttpRequest):
    if request.method == "GET":
        context = {
            "creation_form": PostCreationForm
        }
        return render(
            request, "blog/post_form.html", context=context
        )
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        Post.objects.create(
            owner_id=request.user.pk,
            title=title,
            content=content
        )
        return HttpResponseRedirect(
            reverse_lazy("blog:index")
        )


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["creation_form"] = CommentCreationForm()
        return context


@login_required
def comment_create_view(
        request: HttpRequest,
        pk: int
) -> HttpResponseRedirect:
    if request.method == "POST":

        content = request.POST["content"]

        Commentary.objects.create(
            user_id=request.user.pk,
            post_id=pk,
            content=content
        )
        return HttpResponseRedirect(
            reverse_lazy("blog:post-detail", args=[pk])
        )
