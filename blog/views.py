from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Post, User, Commentary
from blog.forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.order_by("-created_time").select_related("owner")


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
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
