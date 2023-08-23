from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from blog.models import Post, Commentary, User


@login_required
def index(request):

    post = Post.objects.count()
    user = User.objects.count()
    visits = request.session.get("visits", 0)
    request.session["visits"] = visits + 1

    context = {
        "post": post,
        "user": user,
        "visits": visits + 1,
    }

    return render(request, "blog/index.html", context=context)


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post-list")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post-list")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:post-detail")


class CommentaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:post-detail")


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary
    template_name = "blog/commentary_confirm_delete.html"
    success_url = reverse_lazy("blog:post-detail")
