from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return (Post.objects.annotate(
            comment_count=Count("commentaries"))
            .order_by("-created_time")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        content = request.POST.get("content")

        if content:
            Commentary.objects.create(
                user=request.user,
                post=post,
                content=content,
            )

        return redirect(reverse("blog:post-detail", kwargs={"pk": pk}))

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
