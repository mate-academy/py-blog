from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.models import User, Post, Commentary


def index(request):
    num_users = User.objects.count()
    num_posts = Post.objects.count()
    num_comments = Commentary.objects.count()
    post_list = Post.objects.all()[:5]
    context = {
        "num_users": num_users,
        "num_posts": num_posts,
        "num_comments": num_comments,
        "post_list": post_list,
    }
    return render(request, "blog/index.html", context=context)


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "blog/profile.html"
    context_object_name = "profile_user"


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    template_name = "blog/profile_edit.html"

    def get_success_url(self):
        # self.object — это пользователь, который только что сохранился
        return reverse_lazy("blog:profile", kwargs={"pk": self.object.pk})


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = (
        "title",
        "content",
    )
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = (
        "title",
        "content",
    )


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post-list")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("content",)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]  # если pk передается в URL
        return super().form_valid(form)

    def get_success_url(self):

        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )
