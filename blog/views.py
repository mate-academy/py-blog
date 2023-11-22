from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 5
    template_name = "index.html"

    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count("commentaries"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class AddCommentView(CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "add_comment.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )


class UserLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("blog:index")


class UserLogoutView(LogoutView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("blog:index")
