import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


# Create your views here.
class IndexViews(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    ordering = ["created_time"]
    paginate_by = 5


class PostDetailViews(LoginRequiredMixin, generic.DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ("title", "content")
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_delete_form.html"


@login_required
def create_comment(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        content = request.POST["content"]
        post_id = request.POST["post_id"]
        user_id = request.POST["user_id"]
        created_time = datetime.datetime.now()
        Commentary.objects.create(
            content=content,
            post_id=post_id,
            user_id=user_id,
            created_time=created_time,
        )
    return redirect("blog:post-detail", pk=pk,)
