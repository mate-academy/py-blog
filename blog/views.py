from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from blog.forms import CommentForm

from blog.models import Commentary, Post, User


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time").select_related("owner")
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostDetailView(generic.DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=kwargs["pk"])
        if request.user.is_anonymous:
            form.add_error("content", "You must to login for adding comments")
        elif form.is_valid():
            Commentary.objects.create(
                user=request.user,
                post=post,
                **form.cleaned_data
            )
            return HttpResponseRedirect(reverse(
                "blog:post-detail", kwargs={"pk": kwargs["pk"]}
            ))
        context = {"form": form, "post": post}
        return render(request, "blog/post_detail.html", context=context)


class UserDetailView(generic.DetailView):
    model = User
